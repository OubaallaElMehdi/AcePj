package com.ace.userservice.ws;

import com.ace.userservice.entity.User;
import com.ace.userservice.config.JwtUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private com.ace.userservice.service.AuthService userService;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private JwtUtils jwtUtils;

    @PostMapping("/register")
    public String register(@RequestBody User user) {
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        userService.saveUser(user);
        return "User registered successfully!";
    }


    @PostMapping("/login")
    public String login(@RequestBody Map<String, String> request) {
        String username = request.get("username");
        String password = request.get("password");
        User user = userService.findByUsername(username);
        if (passwordEncoder.matches(password, user.getPassword())) {
            return jwtUtils.generateToken(username, user.getRoles());
        } else {
            throw new RuntimeException("Invalid credentials");
        }
    }
}

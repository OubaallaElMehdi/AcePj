package com.ace.vehicleservice.ws;

import com.ace.vehicleservice.entity.Trajectory;
import com.ace.vehicleservice.entity.Vehicle;
import com.ace.vehicleservice.service.TrajectoryService;
import com.ace.vehicleservice.service.VehicleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/trajectories")
public class TrajectoryController {

    private TrajectoryService trajectoryService;


    // Fetch all trajectories for a specific vehicle
    @GetMapping("/vehicle/{vehicleId}")
    public List<Trajectory> getTrajectoriesByVehicle(@PathVariable Long vehicleId) {
        return trajectoryService.getTrajectoriesByVehicleId(vehicleId);
    }
    @PostMapping("/trajectories")
    public Trajectory addTrajectory(@RequestBody Trajectory trajectory) {
        return trajectoryService.save(trajectory);
    }

}

package com.ace.vehicleservice.ws;

import com.ace.vehicleservice.entity.MovementLog;
import com.ace.vehicleservice.repository.MovementLogRepository;
import com.ace.vehicleservice.service.TrajectorySimulator;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/trajectories")
public class TrajectoryController {

    private final TrajectorySimulator trajectorySimulator;
    private final MovementLogRepository movementLogRepository;

    public TrajectoryController(TrajectorySimulator trajectorySimulator, MovementLogRepository movementLogRepository) {
        this.trajectorySimulator = trajectorySimulator;
        this.movementLogRepository = movementLogRepository;
    }

    @PostMapping("/simulate")
    public String simulateTrajectory(@RequestParam Long vehicleId,
                                     @RequestParam double startLat,
                                     @RequestParam double startLon,
                                     @RequestParam double endLat,
                                     @RequestParam double endLon,
                                     @RequestParam double speed,
                                     @RequestParam int intervalInSeconds,
                                     @RequestParam int steps) {
        trajectorySimulator.simulateMovement(vehicleId, new double[]{startLat, startLon}, new double[]{endLat, endLon}, speed, intervalInSeconds, steps);
        return "Trajectory simulation started for vehicle " + vehicleId;
    }

    @GetMapping("/{vehicleId}/location")
    public MovementLog getLatestLocation(@PathVariable Long vehicleId) {
        Optional<MovementLog> latestLog = movementLogRepository.findFirstByVehicleIdOrderByTimestampDesc(vehicleId);
        return latestLog.orElseThrow(() -> new RuntimeException("No location found for vehicle " + vehicleId));
    }
}

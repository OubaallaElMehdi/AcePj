package com.ace.vehicleservice.service;

import com.ace.vehicleservice.entity.Trajectory;
import com.ace.vehicleservice.repository.TrajectoryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TrajectoryService {

    @Autowired
    private TrajectoryRepository trajectoryRepository;

    public Trajectory save(Trajectory trajectory) {
        return trajectoryRepository.save(trajectory);
    }

    public List<Trajectory> getTrajectoriesByVehicleId(Long vehicleId) {
        return trajectoryRepository.findByVehicleId(vehicleId);
    }
}

package com.ace.gateway.acegateway.config;

import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RouteConfig {

    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
                .route("vehicle_service", r -> r.path("/vehicles/**").uri("lb://VEHICLE-SERVICE"))
                .route("user_service", r -> r.path("/users/**").uri("lb://USER-SERVICE"))
                .route("alert_service", r -> r.path("/alerts/**").uri("lb://ALERT-SERVICE"))
                .route("ml_service", r -> r.path("/ml/**").uri("lb://ANOMALY-DETECTION-SERVICE"))
                .build();
    }
}

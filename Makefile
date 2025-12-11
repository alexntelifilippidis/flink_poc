.PHONY: help up down restart logs clean ps status kafka-ui

# Default target
help:
	@echo "Available commands:"
	@echo "  make up          - Start all services"
	@echo "  make down        - Stop all services"
	@echo "  make restart     - Restart all services"
	@echo "  make logs        - View logs from all services"
	@echo "  make logs-f      - Follow logs from all services"
	@echo "  make ps          - List running containers"
	@echo "  make status      - Show status of all services"
	@echo "  make clean       - Stop and remove all containers, networks, and volumes"
	@echo "  make kafka-ui    - Open Kafka UI in browser"
	@echo "  make kafka-logs  - View Kafka logs"
	@echo "  make zk-logs     - View Zookeeper logs"

# Start services
up:
	cd docker && podman-compose up -d

# Stop services
down:
	cd docker && podman-compose down

# Restart services
restart:
	cd docker && podman-compose restart

# View logs
logs:
	cd docker && podman-compose logs

# Follow logs
logs-f:
	cd docker && podman-compose logs -f

# List running containers
ps:
	cd docker && podman-compose ps

# Show status
status:
	cd docker && podman-compose ps

# Clean up everything
clean:
	cd docker && podman-compose down -v

# Open Kafka UI in browser
kafka-ui:
	@echo "Opening Kafka UI at http://localhost:8080"
	@open http://localhost:8080 || xdg-open http://localhost:8080 2>/dev/null || echo "Please open http://localhost:8080 in your browser"

# View Kafka logs
kafka-logs:
	cd docker && podman-compose logs -f kafka

# View Zookeeper logs
zk-logs:
	cd docker && podman-compose logs -f zookeeper


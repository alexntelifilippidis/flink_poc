# 🚀 Real-Time Data Pipeline with Kafka, Flink & ClickHouse

> A comprehensive streaming analytics platform built from the ground up over 12 weeks

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Apache Flink](https://img.shields.io/badge/Apache%20Flink-1.18-red.svg)](https://flink.apache.org/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-3.6-black.svg)](https://kafka.apache.org/)
[![ClickHouse](https://img.shields.io/badge/ClickHouse-23.8-yellow.svg)](https://clickhouse.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📖 Overview

This project demonstrates a production-grade real-time data analytics pipeline that:

- **Captures** events from various sources into Apache Kafka
- **Processes** streams in real-time using Apache Flink
- **Stores** data in ClickHouse (OLAP) and PostgreSQL (transactional)
- **Visualizes** insights through dashboards and REST APIs
- **Monitors** system health with Prometheus & Grafana

**Architecture Overview:**
```
Data Sources → PostgreSQL → Kafka → Flink (Stream Processing) → ClickHouse (Analytics)
                                            ↓                          ↓
                                      Monitoring Stack            REST API + Dashboard
```

---

## ✨ Features

- [ ] **Event-Driven Architecture**: Real-time data ingestion with Kafka
- [ ] **Stream Processing**: Complex event processing with Apache Flink
- [ ] **OLAP Analytics**: High-performance queries with ClickHouse
- [ ] **Metadata Storage**: Relational data management with PostgreSQL
- [ ] **Monitoring**: Full observability with Prometheus & Grafana
- [ ] **Data Quality**: Validation, error handling, and reconciliation
- [ ] **API Layer**: REST endpoints for data access
- [ ] **Visualization**: Real-time dashboards
- [ ] **Containerized**: Complete Docker Compose setup

---

## 🏗️ Architecture

### System Components

| Component | Purpose | Technology |
|-----------|---------|------------|
| **Message Broker** | Event streaming platform | Apache Kafka + Zookeeper |
| **Stream Processor** | Real-time data transformation | Apache Flink (PyFlink) |
| **OLAP Database** | Analytical queries | ClickHouse |
| **OLTP Database** | Transactional data | PostgreSQL |
| **Monitoring** | Metrics & alerts | Prometheus + Grafana |
| **API Layer** | Data access | FastAPI |
| **Visualization** | Dashboards | Streamlit / Grafana |

### Data Flow

```
1. Data Generation → PostgreSQL seed data + synthetic event generators
2. Event Production → Python producers publish to Kafka topics
3. Stream Processing → Flink jobs consume, transform, and aggregate
4. Data Storage → Processed data written to ClickHouse
5. Analytics → REST API queries ClickHouse for insights
6. Monitoring → All components emit metrics to Prometheus
```

---

## 📁 Project Structure

```
flink_poc/
├── src/                          # Source code
│   ├── __init__.py
│   ├── producers/                # Kafka producers
│   │   ├── __init__.py
│   │   ├── kafka_producer.py
│   │   ├── postgres_reader.py
│   │   └── generators/           # Synthetic data generators
│   │       ├── __init__.py
│   │       ├── ecommerce_generator.py
│   │       ├── iot_generator.py
│   │       └── saas_generator.py
│   ├── consumers/                # Kafka consumers
│   │   ├── __init__.py
│   │   └── kafka_consumer.py
│   ├── flink_jobs/               # Flink streaming jobs
│   │   ├── __init__.py
│   │   ├── basic_streaming.py
│   │   ├── transformations/      # Stream transformations
│   │   │   ├── __init__.py
│   │   │   ├── windowed_aggregations.py
│   │   │   ├── enrichment.py
│   │   │   └── stateful_processing.py
│   │   └── aggregations/         # Time-based aggregations
│   │       ├── __init__.py
│   │       ├── minute_aggregations.py
│   │       ├── hourly_aggregations.py
│   │       └── daily_aggregations.py
│   ├── api/                      # REST API
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── analytics.py
│   │   │   └── health.py
│   │   └── dependencies.py
│   ├── dashboard/                # Visualization layer
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── components/
│   │       ├── __init__.py
│   │       └── charts.py
│   ├── models/                   # Data models & schemas
│   │   ├── __init__.py
│   │   ├── events.py
│   │   ├── schemas.py
│   │   └── database.py
│   ├── utils/                    # Utility functions
│   │   ├── __init__.py
│   │   ├── kafka_utils.py
│   │   ├── db_utils.py
│   │   ├── validation.py
│   │   └── metrics.py
│   └── config/                   # Configuration
│       ├── __init__.py
│       ├── settings.py
│       └── logging_config.py
├── docker/                       # Docker configurations
│   ├── docker-compose.yml
│   ├── kafka/
│   │   └── Dockerfile
│   ├── flink/
│   │   └── Dockerfile
│   ├── clickhouse/
│   │   ├── Dockerfile
│   │   └── init-db.sql
│   ├── postgres/
│   │   ├── Dockerfile
│   │   └── init-db.sql
│   └── monitoring/
│       ├── prometheus/
│       │   └── prometheus.yml
│       └── grafana/
│           └── dashboards/
├── configs/                      # YAML configs
│   ├── kafka.yaml
│   ├── flink.yaml
│   ├── clickhouse.yaml
│   └── postgres.yaml
├── scripts/                      # Utility scripts
│   ├── setup_environment.sh
│   ├── start_services.sh
│   ├── stop_services.sh
│   ├── seed_database.py
│   └── run_benchmarks.py
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_producers.py
│   │   ├── test_transformations.py
│   │   └── test_utils.py
│   └── integration/
│       ├── __init__.py
│       ├── test_pipeline.py
│       └── test_api.py
├── data/                         # Data files
│   ├── seed/
│   │   ├── users.json
│   │   ├── products.json
│   │   └── categories.json
│   └── schemas/
│       ├── events_schema.json
│       └── kafka_topics.json
├── docs/                         # Documentation
│   ├── architecture/
│   │   ├── system_design.md
│   │   └── data_flow.md
│   ├── api/
│   │   └── endpoints.md
│   └── setup/
│       ├── local_development.md
│       └── production_deployment.md
├── notebooks/                    # Jupyter notebooks
│   ├── exploratory_analysis.ipynb
│   └── performance_testing.ipynb
├── monitoring/                   # Monitoring configs
│   ├── grafana/
│   │   └── dashboards/
│   │       ├── system_health.json
│   │       └── pipeline_metrics.json
│   └── prometheus/
│       └── alerts.yml
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── pyproject.toml                # Python dependencies (uv)
├── uv.lock                       # Lock file
├── README.md                     # This file
├── LICENSE                       # MIT License
├── PROJECT_ROADMAP.md            # 12-week development plan
└── WEEKLY_PROGRESS.md            # Weekly progress tracker
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.12+**
- **Docker & Docker Compose**
- **uv** (Python package manager)
- **Git**

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/flink_poc.git
cd flink_poc

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python dependencies
uv sync

# Copy environment variables
cp .env.example .env
# Edit .env with your configuration

# Start all services with Docker Compose
cd docker
docker-compose up -d

# Verify services are running
docker-compose ps

# Run database initialization scripts
cd ../scripts
./setup_environment.sh
```

### Quick Start

```bash
# 1. Start the infrastructure
docker-compose -f docker/docker-compose.yml up -d

# 2. Seed the database with initial data
uv run python scripts/seed_database.py

# 3. Start a Kafka producer
uv run python src/producers/kafka_producer.py

# 4. Submit a Flink job
uv run python src/flink_jobs/basic_streaming.py

# 5. Access the services
# - Kafka UI: http://localhost:8080
# - Flink Dashboard: http://localhost:8081
# - Grafana: http://localhost:3000
# - API: http://localhost:8000/docs
```

---

## 📚 Documentation

- **[Project Roadmap](docs/PROJECT_ROADMAP.md)** - 12-week development plan with learning resources
- **[Weekly Progress](docs/WEEKLY_PROGRESS.md)** - Track your 3-hour weekly sessions
- **[Architecture Documentation](docs/architecture/)** - System design and data flow
- **[API Documentation](docs/api/)** - REST API endpoints and usage
- **[Setup Guides](docs/setup/)** - Local development and deployment

---

## 🎯 Use Cases

This project template can be adapted for various domains:

### 🛒 E-Commerce Analytics
- Track user behavior (page views, searches, purchases)
- Analyze conversion funnels and revenue metrics
- Monitor product performance and inventory

### 🌡️ IoT Sensor Platform
- Process sensor readings in real-time
- Detect anomalies and generate alerts
- Predict maintenance needs

### 💼 SaaS Application Monitoring
- Track feature usage and user engagement
- Monitor errors and performance metrics
- Analyze user journey and retention

### 💰 Financial Transaction Processing
- Process transactions in real-time
- Detect fraudulent patterns
- Generate regulatory compliance reports

---

## 🔧 Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run unit tests only
uv run pytest tests/unit/

# Run integration tests
uv run pytest tests/integration/

# Run with coverage
uv run pytest --cov=src tests/
```

### Code Quality

```bash
# Format code
uv run ruff format src/

# Lint code
uv run ruff check src/

# Type checking
uv run mypy src/
```

### Monitoring

Access the monitoring dashboards:

- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090
- **Flink Dashboard**: http://localhost:8081

---

## 📊 Performance

### Benchmarks

| Metric | Target | Current |
|--------|--------|---------|
| Events/second throughput | 10,000+ | TBD |
| End-to-end latency (p99) | < 5s | TBD |
| Query response time (p95) | < 500ms | TBD |
| Data accuracy | 99.9%+ | TBD |

*Benchmarks will be updated as the project progresses*

---

## 🗓️ Development Timeline

This project follows a 12-week learning path with 3-hour weekly sessions:

- **Weeks 1-2**: Foundation (Kafka, PostgreSQL)
- **Weeks 3-4**: Stream Processing (Flink basics & transformations)
- **Weeks 5-6**: OLAP Integration (ClickHouse & pipelines)
- **Weeks 7-8**: Data Generation & Advanced Analytics
- **Weeks 9-10**: Monitoring & Data Quality
- **Weeks 11-12**: Optimization & API Layer

See [PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md) for detailed weekly plans.

---

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

### Learning Resources

- **Apache Kafka**: [Official Documentation](https://kafka.apache.org/documentation/)
- **Apache Flink**: [PyFlink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/overview/)
- **ClickHouse**: [Official Docs](https://clickhouse.com/docs/en/intro)
- **Stream Processing**: [Designing Data-Intensive Applications](https://dataintensive.net/) by Martin Kleppmann

### Communities

- [Confluent Community (Kafka)](https://www.confluent.io/community/)
- [Apache Flink Community](https://flink.apache.org/community.html)
- [ClickHouse Community](https://clickhouse.com/community)

---

## 📧 Contact

**Project Maintainer**: [Your Name]

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

---

## 🎓 Learning Journey

Track your progress in [WEEKLY_PROGRESS.md](docs/WEEKLY_PROGRESS.md)

**Current Week**: Week 1  
**Total Hours**: 0/36  
**Completion**: 0%

---

## 🔮 Future Enhancements

- [ ] Add schema registry (Confluent Schema Registry)
- [ ] Implement exactly-once semantics
- [ ] Add machine learning model serving
- [ ] Implement CDC (Change Data Capture) from PostgreSQL
- [ ] Add Redis caching layer
- [ ] Kubernetes deployment manifests
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Multi-region support
- [ ] A/B testing framework
- [ ] Real-time recommendation engine

---

<div align="center">
  
**Built with ❤️ as a learning journey into real-time data engineering**

⭐ Star this repo if you find it helpful!

</div>


# Wallet

## Overview
Wallet is a personal project designed to read, process, and classify bank statements efficiently. It's useful for understanding monthly expenses and organizing personal finances. This application helps users manage their financial data by categorizing transactions and providing insights into spending patterns.

## Features
- **Automated Bank Statement Processing**: Automatically reads and processes bank statements in various formats.
- **Expense Classification**: Categorizes expenses to help users understand their spending habits.
- **Monthly Reports**: Generates monthly financial reports for better budget tracking.
- **Data Visualization**: Visual representation of spending trends over time.

## Getting Started

### Prerequisites
To run this project, you need to have Docker and Docker Compose installed on your machine.

- **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)

### Setup & Run
1. Start containers: ```docker-compose -f .docker-compose/docker-compose.yml up```
2. Add statements on src/resources
3. Run: ```python main.py```
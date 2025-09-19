# Automobile Sales Dashboard

## Project Overview

This project is a comprehensive dashboard application built with **Plotly Dash** to analyze historical trends in automobile sales during recession periods. The primary objective is to provide insights into how the sales of **XYZAutomotives**, a company specializing in automotive sales, were affected during times of economic recession.

### Key Features

- Interactive dashboard with dropdown menus for data filtering
- Recession period analysis with multiple visualization types
- Yearly statistics and trends analysis
- Real-time data visualization using Plotly charts
- Responsive design for different screen sizes

## Project Structure

```
automobile-sales-dashboard/
├── src/
│   └── dashapp.py          # Main dashboard application
├── data/                   # Data files (local copies)
├── assets/                 # CSS, images, and other static assets
├── docs/                   # Project documentation
├── tests/                  # Unit tests
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore             # Git ignore file
```

## Data Source

The dashboard uses historical automobile sales data sourced from:
- **Dataset URL**: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv

### Data Schema

The dataset includes the following key columns:
- `Year`: Year of sales data
- `Month`: Month of sales data
- `Automobile_Sales`: Number of automobiles sold
- `Vehicle_Type`: Type of vehicle (e.g., sedan, SUV, etc.)
- `Recession`: Binary indicator (1 = recession period, 0 = non-recession)
- `Unemployment_Rate`: Unemployment rate during the period
- `Advertising_Expenditure`: Marketing expenditure for vehicles

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the project**:
   ```bash
   cd automobile-sales-dashboard
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Dashboard

1. **Start the development server**:
   ```bash
   python src/dashapp.py
   ```

2. **Access the dashboard**:
   Open your web browser and navigate to `http://127.0.0.1:8050/`

### Dashboard Features

#### 1. Recession Period Statistics
- **Average Automobile Sales**: Line chart showing sales fluctuation over recession periods
- **Sales by Vehicle Type**: Bar chart displaying average sales by vehicle category
- **Expenditure Share**: Pie chart showing advertising expenditure distribution
- **Unemployment Impact**: Bar chart analyzing the effect of unemployment rates on sales

#### 2. Yearly Statistics
- **Annual Sales Trend**: Line chart showing overall sales trends
- **Monthly Sales Pattern**: Line chart displaying seasonal sales patterns
- **Vehicle Type Performance**: Bar chart showing average sales by vehicle type for selected year
- **Advertisement Expenditure**: Pie chart showing marketing spend distribution

## Development

### Code Structure

The main application (`src/dashapp.py`) follows this structure:

1. **Data Loading**: Fetches historical automobile sales data
2. **Layout Definition**: Creates the dashboard UI with dropdowns and output containers
3. **Callback Functions**: Handles user interactions and updates visualizations
4. **Chart Generation**: Creates Plotly visualizations based on selected filters

### Key Components

- **Dropdown Menus**: Statistics type and year selection
- **Interactive Charts**: Plotly visualizations that update based on user input
- **Responsive Layout**: HTML/CSS structure for optimal viewing

## Analysis Insights

### Recession Impact Analysis

The dashboard provides insights into:

1. **Sales Volume Changes**: How automobile sales fluctuated during recession periods
2. **Vehicle Type Preferences**: Which vehicle types were more resilient during recessions
3. **Marketing Effectiveness**: Advertising expenditure patterns during economic downturns
4. **Economic Correlation**: Relationship between unemployment rates and automobile sales

### Business Value

- **Strategic Planning**: Helps XYZAutomotives plan for future economic uncertainties
- **Market Understanding**: Provides deeper insights into consumer behavior during recessions
- **Resource Allocation**: Guides marketing and inventory decisions
- **Risk Assessment**: Enables better preparation for economic downturns

## Technical Requirements

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| dash | >=2.14.1 | Web application framework |
| plotly | >=5.17.0 | Interactive visualizations |
| pandas | >=2.0.3 | Data manipulation and analysis |
| more-itertools | >=10.1.0 | Additional iteration tools |
| numpy | >=1.24.3 | Numerical computing |
| gunicorn | >=21.2.0 | Production WSGI server |

### Browser Compatibility

- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 79+

## Deployment

### Local Development
```bash
python src/dashapp.py
```

### Production Deployment
```bash
gunicorn --bind 0.0.0.0:8000 src.dashapp:server
```

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed via `pip install -r requirements.txt`
2. **Data Loading Issues**: Check internet connection for CSV data fetching
3. **Port Conflicts**: Change the port in `dashapp.py` if 8050 is already in use

### Support

For issues or questions:
- Check the documentation in the `docs/` folder
- Review the code comments in `src/dashapp.py`
- Create an issue in the project repository

## License

This project is for educational and analytical purposes. Please ensure compliance with data usage terms and conditions.

## Acknowledgments

- Data provided by IBM Developer Skills Network
- Built with Plotly Dash framework
- Inspired by real-world automotive industry analysis needs
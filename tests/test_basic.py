#!/usr/bin/env python
"""
Basic tests for the automobile sales dashboard
"""

import pytest
import pandas as pd
import dash
from dash import dcc, html


class TestBasicSetup:
    """Test basic setup and dependencies"""
    
    def test_imports(self):
        """Test that all required packages can be imported"""
        import dash
        import plotly.graph_objs as go
        import plotly.express as px
        import pandas as pd
        import more_itertools
        assert True  # If we get here, imports worked
    
    def test_data_loading(self):
        """Test that the data can be loaded from the URL"""
        data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
        data = pd.read_csv(data_url)
        
        # Check basic properties
        assert data.shape[0] > 0, "Data should have rows"
        assert data.shape[1] > 0, "Data should have columns"
        
        # Check for expected columns
        expected_columns = ['Year', 'Month', 'Automobile_Sales', 'Vehicle_Type', 'Recession']
        for col in expected_columns:
            assert col in data.columns, f"Column {col} should be present in the data"
    
    def test_dash_app_creation(self):
        """Test that a basic Dash app can be created"""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            html.H1("Test Dashboard"),
            dcc.Graph(id='test-graph')
        ])
        
        assert app is not None
        assert app.layout is not None


class TestDataAnalysis:
    """Test data analysis functions"""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing"""
        return pd.DataFrame({
            'Year': [2008, 2009, 2010, 2011],
            'Month': [1, 2, 3, 4],
            'Automobile_Sales': [1000, 800, 1200, 1100],
            'Vehicle_Type': ['Sedan', 'SUV', 'Sedan', 'SUV'],
            'Recession': [1, 1, 0, 0],
            'unemployment_rate': [7.5, 8.0, 6.5, 6.0],
            'Advertising_Expenditure': [50000, 40000, 60000, 55000]
        })
    
    def test_recession_data_filtering(self, sample_data):
        """Test filtering data for recession periods"""
        recession_data = sample_data[sample_data['Recession'] == 1]
        
        assert len(recession_data) == 2, "Should have 2 recession period records"
        assert all(recession_data['Recession'] == 1), "All records should have Recession = 1"
    
    def test_yearly_grouping(self, sample_data):
        """Test grouping data by year"""
        yearly_data = sample_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        
        assert len(yearly_data) == 4, "Should have 4 years of data"
        assert 'Year' in yearly_data.columns
        assert 'Automobile_Sales' in yearly_data.columns


if __name__ == "__main__":
    pytest.main([__file__])
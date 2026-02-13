"""Shared pytest fixtures and configuration for climate ETL tests"""

import pytest
import tempfile
import shutil
import pandas as pd
import geopandas as gpd
from pathlib import Path


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files"""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_centroids_csv(temp_dir):
    """Create a sample centroids CSV file"""
    csv_path = Path(temp_dir) / "centroids.csv"
    df = pd.DataFrame({
        'FID': [1, 2, 3],
        'lon': [-53.9, -53.8, -53.85],
        'lat': [-12.1, -12.2, -12.15]
    })
    df.to_csv(csv_path, index=False)
    return str(csv_path)


@pytest.fixture
def sample_centroids_shp(temp_dir):
    """Create a sample centroids shapefile"""
    shp_path = Path(temp_dir) / "centroids.shp"
    gdf = gpd.GeoDataFrame({
        'FID': [1, 2, 3],
    }, geometry=gpd.points_from_xy([-53.9, -53.8, -53.85], [-12.1, -12.2, -12.15]))
    gdf.to_file(shp_path)
    return str(shp_path)

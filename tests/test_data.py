"""Tests for data loading utilities."""

import pandas as pd

from src.utils.data import load_test_data, load_train_data


def test_load_train_data_returns_dataframe():
    """Given train.csv exists, When calling load_train_data, Then returns a DataFrame."""
    df = load_train_data()
    assert isinstance(df, pd.DataFrame)


def test_load_train_data_shape():
    """Given train.csv has 22500 rows, When loading, Then shape matches."""
    df = load_train_data()
    assert len(df) == 22500


def test_load_train_data_has_subscribe():
    """Given train.csv, When loading, Then subscribe column exists."""
    df = load_train_data()
    assert "subscribe" in df.columns
    assert set(df["subscribe"].unique()).issubset({"yes", "no"})


def test_load_train_data_column_count():
    """Given train.csv, When loading, Then has 22 columns (id + 20 features + subscribe)."""
    df = load_train_data()
    assert len(df.columns) == 22


def test_load_test_data_returns_dataframe():
    """Given test.csv exists, When calling load_test_data, Then returns a DataFrame."""
    df = load_test_data()
    assert isinstance(df, pd.DataFrame)


def test_load_test_data_shape():
    """Given test.csv has 7500 rows, When loading, Then shape matches."""
    df = load_test_data()
    assert len(df) == 7500


def test_load_test_data_no_subscribe():
    """Given test.csv has no labels, When loading, Then subscribe column does not exist."""
    df = load_test_data()
    assert "subscribe" not in df.columns


def test_load_test_data_column_count():
    """Given test.csv, When loading, Then has 21 columns (id + 20 features)."""
    df = load_test_data()
    assert len(df.columns) == 21

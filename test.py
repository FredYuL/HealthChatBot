import pytest
from app import app
from functions import calculate_bmi, create_workout_plan_with_BMI
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_workout_plan():
    """Test workout plan generation."""
    response = create_workout_plan_with_BMI("beginner", "Healthy Weight")
    assert "beginner" in response.lower()
    assert "maintaining your weight" in response.lower() 


def test_personalized_workout_beginner():
    """Test personalized workout for a beginner."""
    response = create_workout_plan_with_BMI("beginner", "Underweight")
    assert "beginner" in response.lower()
    assert "gaining weight in a healthy way" in response.lower()


def test_personalized_workout_intermediate():
    """Test personalized workout for an intermediate user."""
    response = create_workout_plan_with_BMI("intermediate", "Healthy Weight")
    assert "intermediate" in response.lower()
    assert "maintaining your weight" in response.lower()  


def test_personalized_workout_advanced():
    """Test personalized workout for an advanced user."""
    response = create_workout_plan_with_BMI("advanced", "Obese")
    assert "advanced" in response.lower()
    assert "losing weight in a healthy way" in response.lower()  

def test_open_google(driver):
    assert "Automation Exercise" in driver.title  # Likely to fail unless URL is Google

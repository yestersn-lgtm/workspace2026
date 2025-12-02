# This is a sample Python script.

config = {
    "debug": True,
    "max_connections": 100,
    "timeout": 30.5,
    "features": ["authentication", "logging", "caching"],
}
print(f"Config Type: {type(config)}")
print(f"Config Content: {config}")

# Constructor
config_dict = dict(
    debug=True,
    max_connections=100,
    timeout=30.5,
    features=["authentication", "logging", "caching"],
)
print(f"Config Dict Type: {type(config_dict)}")
print(f"Config Dict Content: {config_dict}")

user = dict(name="Reese", role="admin", active=True)
print(f"User Type: {type(user)}")
print(f"User Content: {user}")

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    pass

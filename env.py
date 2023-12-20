import os

STRIPE_SECRET_KEY="sk_test_51NS5qfEcKFRGV4ZzSPm3vETAF6uSAyOOAaeB3139RY7Koz5I7AG7akFagCtKRgqmlZJzEGDS5p5cfztXDbSSLDOh00Gtj08EXT"
STRIPE_PUBLIC_KEY="pk_test_51NS5qfEcKFRGV4ZzCXs6oHUl3GW74pBAoqv3tEApwrXrMETbZtgapXBzR6NiTggEVZIKdlCNy9IefLpWqdpWAQzT00SxHbF0yx"

os.environ["DATABASE_URL"] = "postgres://lelfuole:sBx9iFQZN7c-uqX7_r2Da23zg8vuUkb2@surus.db.elephantsql.com/lelfuole"
os.environ["SECRET_KEY"] = "randomkey123..."
import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/abhis/Documents/GitHub/salary/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df
from pathlib import Path
import os
from typing import Tuple

PROJECT_DIR = Path(__file__).parent.parent
DATA_DIR = PROJECT_DIR / 'data'
DATASET_DIR = PROJECT_DIR / 'datasets'
I18N_DIR = PROJECT_DIR / 'i18n'
DATASET_PATH = DATASET_DIR / 'en.openfoodfacts.org.products.csv'
JSONL_DATASET_PATH = DATASET_DIR / 'products.jsonl.gz'
JSONL_DATASET_ETAG_PATH = DATASET_DIR / 'products-etag.txt'
JSONL_MIN_DATASET_PATH = DATASET_DIR / 'products-min.jsonl.gz'
JSONL_DATASET_URL = "https://static.openfoodfacts.org/data/openfoodfacts-products.jsonl.gz"

TAXONOMY_CATEGORY_URL = "https://static.openfoodfacts.org/data/taxonomies/categories.json"
TAXONOMY_INGREDIENT_URL = "https://static.openfoodfacts.org/data/taxonomies/ingredients.json"
TAXONOMY_LABEL_URL = "https://static.openfoodfacts.org/data/taxonomies/labels.json"
OFF_IMAGE_BASE_URL = "https://static.openfoodfacts.org/images/products"
OFF_BASE_WEBSITE_URL = "https://world.openfoodfacts.org"

TAXONOMY_DIR = DATA_DIR / 'taxonomies'
TAXONOMY_CATEGORY_PATH = TAXONOMY_DIR / 'categories.json'
TAXONOMY_INGREDIENT_PATH = TAXONOMY_DIR / 'ingredients.json'
TAXONOMY_LABEL_PATH = TAXONOMY_DIR / 'labels.json'

MODELS_DIR = PROJECT_DIR / 'models'

DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_HOST = os.environ.get("DB_HOST", "localhost")

IPC_AUTHKEY = os.environ.get("IPC_AUTHKEY", "IPC").encode('utf-8')
IPC_HOST = os.environ.get("IPC_HOST", "localhost")
IPC_PORT = int(os.environ.get("IPC_PORT", 6650))
IPC_ADDRESS: Tuple[str, int] = (IPC_HOST, IPC_PORT)
WORKER_COUNT = os.environ.get("WORKER_COUNT", 4)

ELASTICSEARCH_HOSTS = os.environ.get("ELASTICSEARCH_HOSTS", "localhost:9200").split(",")
ELASTICSEARCH_TYPE = "document"

ELASTICSEARCH_CATEGORY_INDEX = 'category'
ELASTICSEARCH_PRODUCT_INDEX = 'product'

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', "")
SLACK_OFF_TEST_CHANNEL = "CGLCKGVHS"
SLACK_OFF_ROBOTOFF_ALERT_CHANNEL = "CGKPALRCG"

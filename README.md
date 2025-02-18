## __🛒 Django Shop__
![Django](https://img.shields.io/badge/Django-4.2-blue?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge)
## Description project
On this store website, I used CRUD capabilities. Product search via PostgreSQL using ``` django.contrib.postgres.search```. Added similar products by category to the products.
Created a cart into which data is recorded using sessions and with their help shows the purchase.
Order processing and sending the number to email are organized using Celery to reduce waiting time.
Discounts and coupons have been added to the products. Each discount and coupon can be added in the admin panel. In addition, they will disappear if their validity period expires. Added payment via Stripe, which takes into account both discounts and coupons. The project itself was deployed on RailWay.

🚀 Deploy on Railway
The project is deployed on Railway.
To check the operation of the site, go to the link:
🔗https://shopfurnitures.up.railway.app/

## 🚀 Functional
✔️ Categories and products  
✔️ CRUD on products  
✔️ Product search  
✔️ Throwing goods into the basket
✔️ Placing an order
✔️ Sending a message to email
✔️ Coupons and discounts
✔️ Payment via stripe
✔️ Webhook

## 🛠️ Технології
- **Django**
- **PostgreSQL**
- **Celery + Redis**
- **Celery + Beat**
- **Cloudinary**
- **Railway**

## 📦 Installation and local launch

1️⃣ Cloning the repository
```bash
git clone https://github.com/AMuhailo/Django-Shop-Project.git
cd Django-Shop-Project.git
```

2️⃣ Virtual environment
```bash
python -m venv venv
source venv/bin/activate # for macOS and Linux
venv\Scripts\activate # for Windows
```

3️⃣ Installing dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Setting Environment Variables
To run locally, you need to create an .env file in the root folder:
```bash
ENVIRONMENT=development
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://postgres:AXeLLOVEXmumFmvnANIkEAwEsfPUQSZH@autorack.proxy.rlwy.net:18205/railway
CLOUDINARY_URL=cloudinary://769593718786664:Px0Uwth8JONclxSNGJM9fZGbP9Q@dmzji9ijo
REDIS_PUBLIC_URL=redis://default:MwVRdhmiDcLHtZUqzfMwZTJVdmcAstZu@monorail.proxy.rlwy.net:42048
REDIS_URL=redis://default:MwVRdhmiDcLHtZUqzfMwZTJVdmcAstZu@redis.railway.internal:6379
EMAIL_HOST_PASSWORD=your-password-app-gmail
EMAIL_HOST_USER=your-email
STRIPE_SECRET_KEY_TEST=your-stripe-secret-key
STRIPE_WEBHOOK_SECRET=your-webhooks-secret-key
```
⚠️ Don't upload .env to GitHub!
It needs to be added to .gitignore.

5️⃣ Starting the server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
The site is now available at http://127.0.0.1:8000.

## ⚡Launching Celery
To allow Celery to run tasks in the background, start it like this:
```bash
celery -A myshop worker --loglevel=info
```

## 🔗 Useful commands
💾 Creating a database backup
```bash
python manage.py dumpdata --indent=2 --output=shop/fixtures/db_backup.json
```

♻️ Database recovery
```bash
python manage.py loaddata db_backup.json
```
# Diet Planner using Machine Learning (Sanitized)

**Short:** Educational demo: diet recommendation proof-of-concept using ML with a Django front-end.
**Warning:** This repository is sanitized for public release. It does **not** include any real/personal data, institutional logos, or trained model artifacts. Do not use this project as medical advice.

---

## What’s included
- Django app skeleton (`diet_project` / `diet_app`) with safe auth & prediction view (sanitized).
- `Dataset/sample_dataset.csv` — small synthetic dataset (no real data).
- `.gitignore` to avoid committing models/datasets/secrets.
- `requirements.txt` with required Python packages.
- `train_model.py` — example script to train a pipeline and save it to `Model/diet_pipeline.joblib` (runs locally).

---

## Quickstart (local)
1. Clone or download this repo and navigate into it:
```bash
cd diet-planner-ml-sanitized
```

2. Create & activate venv:
```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate       # Windows
```

3. Install:
```bash
pip install -r requirements.txt
```

4. Setup environment variables (create `.env` in project root — see `.env.example`):
```text
SECRET_KEY=your_django_secret_here
DEBUG=True
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=
```

5. Migrate & run (this repo contains minimal skeleton; adapt to your project):
```bash
python manage.py migrate
python manage.py createsuperuser  # optional, for admin
python manage.py runserver
```

6. Add your **own** dataset and trained model:
- Do **not** commit `Dataset/` or `Model/` to git.
- Place dataset at `Dataset/sample_dataset.csv` locally and trained model at `Model/diet_pipeline.joblib` (or use environment-based storage).
- See `train_model.py` for training steps (example).

---

## How to safely add a model/dataset
- Use `.gitignore` to exclude `Dataset/` and `Model/`.
- Use GitHub Releases, Google Drive, or a private S3 bucket to host large assets; add download instructions to README.
- If dataset contains personal data, anonymize before using.

---

## Security & privacy checklist (before publishing)
- [ ] Remove personal names or get permission from teammates.
- [ ] Remove college logos or get explicit permission.
- [ ] Ensure no real personal health data (PHI) in `Dataset/`.
- [ ] Replace debug secrets with environment variables.

---

## License
Choose an open-source license (e.g. MIT). Add `LICENSE` file if you intend to open-source.


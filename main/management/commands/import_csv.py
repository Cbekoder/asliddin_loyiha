import os
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from main.models import ScoreEntry  # Import your model

class Command(BaseCommand):
    help = "Import CSV data into the database"

    def handle(self, *args, **kwargs):
        BASE_DIR = settings.BASE_DIR
        file_paths = [
            os.path.join(BASE_DIR, "files", "baza.csv"),
            os.path.join(BASE_DIR, "files", "full.edit.csv"),
        ]

        for file_path in file_paths:
            if not os.path.exists(file_path):
                self.stdout.write(self.style.ERROR(f"❌ File not found: {file_path}"))
                continue

            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                count_added = 0
                count_skipped = 0

                for row in reader:
                    text = row["Text"]
                    idx = int(row["idx"])
                    score = row["Score"]

                    # Try to create, if exists, skip
                    obj, created = ScoreEntry.objects.get_or_create(
                        text=text,
                        defaults={"idx": idx, "score": score}
                    )
                    print(score, text)
                    if created:
                        count_added += 1
                    else:
                        count_skipped += 1

                self.stdout.write(self.style.SUCCESS(f"✅ Imported {count_added} new records from {file_path}"))
                self.stdout.write(self.style.WARNING(f"⚠️ Skipped {count_skipped} existing records from {file_path}"))

        self.stdout.write(self.style.SUCCESS("🎉 Import completed successfully!"))

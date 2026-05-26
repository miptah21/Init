# Menggunakan image dasar Playwright resmi yang sudah dilengkapi dependencies browser Chromium
FROM mcr.microsoft.com/playwright:v1.45.0-jammy

# Set non-interactive mode untuk apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Update system dan pasang Python 3, pip, serta Linux fonts untuk mendukung stealth emoji & canvas checks
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    # Font Setup: Sangat krusial untuk melewati anti-bot canvas finger-printing (Kasada, Akamai)
    fonts-noto-color-emoji \
    fonts-freefont-ttf \
    fonts-unifont \
    fonts-ipafont-gothic \
    fonts-wqy-zenhei \
    fonts-tlwg-loma-otf \
    && rm -rf /var/lib/apt/lists/*

# Set directory kerja dalam container
WORKDIR /app

# Salin script evaluasi dan dependencies
COPY evaluate_stealth.py .

# Pasang package Python & Node.js untuk otomatisasi browser
# Pasang cloakbrowser dengan geoip support untuk auto timezone/locale detection
RUN pip3 install --no-cache-dir \
    playwright \
    "cloakbrowser[geoip]"

# Pasang package cloakbrowser Node.js jika menggunakan JS/TS script
RUN npm install -g cloakbrowser playwright-core

# Pre-download & cache biner Chromium stealth (~200MB) saat proses build image.
# Ini mencegah keterlambatan / download berulang kali di startup container.
ENV CLOAKBROWSER_CACHE_DIR=/root/.cache/cloakbrowser
RUN python3 -m cloakbrowser install

# Jalankan script evaluasi secara default
CMD ["python3", "evaluate_stealth.py"]

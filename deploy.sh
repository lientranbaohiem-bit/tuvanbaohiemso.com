#!/usr/bin/env bash
# ============================================================
# Deploy tuvanbaohiemso.com lên GitHub Pages
#
# Dùng:
#   GITHUB_USER=<ten-tai-khoan> GITHUB_TOKEN=<token> ./deploy.sh [ten-repo]
#
# Mặc định tên repo: tuvanbaohiemso
# Repo PHẢI được tạo sẵn trên github.com trước khi chạy script này.
# ============================================================
set -euo pipefail

REPO="${1:-tuvanbaohiemso}"
: "${GITHUB_TOKEN:?Thieu GITHUB_TOKEN — tao tai https://github.com/settings/tokens (scope: repo)}"
: "${GITHUB_USER:?Thieu GITHUB_USER — ten tai khoan GitHub cua ban}"

echo "==> Dung lai site tu build.py..."
python3 build.py

echo "==> Chuan bi git..."
git init -q 2>/dev/null || true
git add -A
git -c user.name="${GITHUB_USER}" \
    -c user.email="${GITHUB_USER}@users.noreply.github.com" \
    commit -qm "Deploy tuvanbaohiemso.com" || echo "    (khong co thay doi moi)"
git branch -M main

echo "==> Day code len ${GITHUB_USER}/${REPO}..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${REPO}.git"
git push -u origin main --force
git remote set-url origin "https://github.com/${GITHUB_USER}/${REPO}.git"   # go token khoi config

echo ""
echo "============================================================"
echo " Da push xong."
echo ""
echo " CON 2 BUOC LAM TREN GIAO DIEN GITHUB (1 phut):"
echo ""
echo " 1. Vao: https://github.com/${GITHUB_USER}/${REPO}/settings/pages"
echo "    - Source: Deploy from a branch"
echo "    - Branch: main  /  (root)  -> Save"
echo ""
echo " 2. Cung trang do, muc Custom domain:"
echo "    - Nhap: tuvanbaohiemso.com  -> Save"
echo "    - Tick 'Enforce HTTPS' (doi 5-30 phut sau khi DNS da tro dung)"
echo ""
echo " DNS can tro tai nha cung cap ten mien:"
echo "    A      @      185.199.108.153"
echo "    A      @      185.199.109.153"
echo "    A      @      185.199.110.153"
echo "    A      @      185.199.111.153"
echo "    CNAME  www    ${GITHUB_USER}.github.io"
echo ""
echo " Web se chay tai: https://tuvanbaohiemso.com"
echo " (tam thoi cung xem duoc tai https://${GITHUB_USER}.github.io/${REPO}/)"
echo "============================================================"

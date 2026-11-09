# Projekt: AutoFPL-Manager (Autonomiczny Agent Optymalizacyjny)

## Cel projektu i Architektura
Stworzyłem autonomiczny system w Pythonie do optymalizacji składu w grze Fantasy Premier League. Projekt łączy inżynierię danych (ETL), klasyczne uczenie maszynowe oraz badania operacyjne, działając całkowicie w chmurze.

## Uczenie Maszynowe i Predykcje (LightGBM)
Zaprojektowałem i wytrenowałem modele LightGBM do przewidywania punktów zawodników. Wymagało to przetworzenia dużych zbiorów danych historycznych, inżynierii cech (feature engineering) oraz radzenia sobie z problemami takimi jak brakujące dane z powodu kontuzji.

## Optymalizacja Matematyczna (MILP)
Do maksymalizacji oczekiwanej liczby punktów przy zachowaniu zasad gry (budżet, limity transferów, formacje) zaimplementowałem solver Mixed-Integer Linear Programming (MILP) przy użyciu biblioteki Google OR-Tools.

## MLOps, CI/CD i Wdrożenie (Docker, GitHub Actions)
Skomponowałem pełen pipeline MLOps. Aplikacja jest skonteneryzowana za pomocą Dockera. Automatyzację uruchamiania raportów i rozwiązywania zależności solvera obsługuje GitHub Actions. Zaimplementowałem uwierzytelnianie SSH do repozytorium bez użycia haseł, co pozwala systemowi na w pełni autonomiczne commity z wynikami analiz.

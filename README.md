# DevOps + Git – Mini-projet pratique

Un petit projet **Python + CI GitHub Actions** pour pratiquer Git dans un contexte DevOps.

## 🎯 Objectifs
- Savoir initialiser un dépôt, créer des branches et faire des PR.
- Mettre en place une **CI** simple (tests `pytest`).
- Résoudre un **conflit de merge**.
- Créer une **release** et un **tag**.
- Corriger un bug pour faire passer la CI au vert.

---

## 🗂️ Structure
```
devops-git-workshop/
├─ app/
│  └─ calculator.py
├─ tests/
│  └─ test_calculator.py
├─ .github/workflows/python-ci.yml
├─ requirements.txt
├─ .gitignore
└─ README.md
```

---

## 🧪 Application (buggée exprès)
`app/calculator.py` expose 4 fonctions (`add`, `sub`, `mul`, `div`). La division contient un **bug** (division entière au lieu de flottante). Les tests `pytest` détectent ce bug.

---

## 🚀 Parcours pas-à-pas

### 0) Pré-requis
- Python 3.10+ installé
- Un compte GitHub
- `git` installé

### 1) Initialiser le dépôt local
```bash
git init
git branch -M main
git add .
git commit -m "Initial commit: workshop skeleton"
```

### 2) Créer le dépôt distant
Crée un repo vide sur GitHub (sans README auto). Puis :
```bash
git remote add origin https://github.com/<ton-user>/devops-git-workshop.git
git push -u origin main
```

### 3) Activer la CI (GitHub Actions)
La CI est déjà configurée via `.github/workflows/python-ci.yml`. À chaque `push`, GitHub va :
- Installer Python
- Installer `pytest`
- Lancer les tests

> Tu verras au premier push que la CI **échoue** (à cause du bug volontaire).

### 4) Feature branch + PR
Crée une branche de correction :
```bash
git checkout -b fix/division-float
# Corrige le bug dans app/calculator.py (utiliser / au lieu de //)
git add app/calculator.py
git commit -m "Fix: division uses true float division"
git push -u origin fix/division-float
```
Ouvre une **Pull Request** sur GitHub de `fix/division-float` vers `main`. Attends que la CI passe **au vert**, puis merge.

### 5) Exercice conflit de merge
Simule un conflit :
1. Sur `main`, modifie **la même ligne** dans `app/calculator.py` (par ex. change le nom de variable ou un commentaire sur la fonction `add`) :
   ```bash
   git checkout -b chore/docs-inline
   # Édite la même ligne que quelqu'un d'autre va modifier
   git commit -am "Docs: adjust inline comment in add()"
   git push -u origin chore/docs-inline
   ```
2. Pendant ce temps, dans une autre branche (ou avec un collègue), modifie **exactement la même ligne** d’une autre manière et pousse la branche.
3. Ouvre deux PRs et tente de merger – GitHub signalera un **conflit**.
4. Résous le conflit en local :
   ```bash
   git checkout main
   git pull
   git checkout chore/docs-inline
   git merge main   # conflit
   # Résous manuellement les marqueurs <<<<<<< ======= >>>>>>>
   git add app/calculator.py
   git commit
   git push
   ```
5. Reviens sur GitHub et finalise la PR.

### 6) Tag & Release
Quand `main` est propre et la CI verte :
```bash
git checkout main
git pull
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0
```
Crée ensuite une **Release** sur GitHub à partir du tag `v1.0.0` avec notes de version.

### 7) (Optionnel) Protection de branche
- Active la protection de `main` (PR obligatoire, 1 review, CI verte, no force-push).

### 8) (Optionnel) Hook pre-commit (local)
Installe `pre-commit` et configure un hook simple (flake8, black, etc.) si souhaité.

---

## ✅ Critères d’évaluation
- [ ] Repo en ligne avec README propre
- [ ] CI passe au vert
- [ ] Au moins 1 PR fusionnée
- [ ] 1 conflit de merge résolu
- [ ] 1 tag + 1 release publiés
- [ ] Historique de commits clair (messages explicites)

---

## 🧰 Commandes utiles mémo
```bash
git status
git log --oneline --graph --decorate --all
git diff
git restore --staged <fichier>
git stash push -m "wip" && git stash pop
git rebase -i HEAD~3
```

Bon atelier !
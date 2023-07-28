<<<<<<< HEAD
echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
=======
pip install -r requirements.txt
python3.9 manage.py collectstatic
>>>>>>> 9771c80cd18a84760d298cae968cf8756443c6de

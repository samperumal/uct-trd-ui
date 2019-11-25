source venv/bin/activate
export LD_LIBRARY_PATH=/home/trd/summer_school_2019/dim_v20r26/linux:$LD_LIBRARY_PATH
export FLASK_ENV=development
export FLASK_APP=flaskr
export DIMDIR=/home/trd/summer_school_2019/dim_v20r26
python run-socket.py alicetrd.phy.uct.ac.za 5002

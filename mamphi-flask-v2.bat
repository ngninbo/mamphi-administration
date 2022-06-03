cd "mamphi-api/api"

START dist/mamphiApi/mamphiApi.exe

cd "../../mamphi-flask-v2/"

CALL c://Users/biocl/Anaconda3/Scripts/activate ai

SET FLASK_APP=app
SET FLASK_DEBUG=1

flask run --port 8081 --host=0.0.0.0

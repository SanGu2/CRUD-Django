# test_connection.py
import mongoengine
from datetime import datetime

MONGODB_URI = "mongodb+srv://localhost:bankofdates@cluster0.neeqr7a.mongodb.net/?appName=Cluster0"

try:
    mongoengine.connect(host=MONGODB_URI)
    print("✅ Conectado ao MongoDB Atlas!")
    
    # Teste de leitura/escrita
    from mongoengine import Document, StringField
    class TestDoc(Document):
        msg = StringField()
    
    TestDoc(msg=f"Teste em {datetime.now()}").save()
    print(f"✅ Documento salvo! Total: {TestDoc.objects.count()}")
    
except Exception as e:
    print(f"❌ Erro: {e}")
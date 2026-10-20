from src.workflow import executer

DEMO = [
    {"source": "jenkins", "type": "build", "severite": "warning",
     "message": "echec du build, password=Sup3rS3cret", "horodatage": "2026-01-01T17:00:00"},
    {"source": "jenkins", "type": "build", "severite": "warning",
     "message": "echec du build, password=Sup3rS3cret", "horodatage": "2026-01-01T17:00:00"},
    {"source": "k8s", "type": "pod", "severite": "erreur",
     "message": "CrashLoopBackOff api-gateway", "horodatage": "2026-01-01T17:00:01"},
    {"source": "k8s", "type": "pod", "severite": "erreur",
     "message": "CrashLoopBackOff api-gateway", "horodatage": "2026-01-01T17:00:02"},
    {"source": "k8s", "type": "pod", "severite": "erreur",
     "message": "CrashLoopBackOff api-gateway", "horodatage": "2026-01-01T17:00:03"},
    {"source": "trivy", "type": "scan", "severite": "critique",
     "message": "CVE-2026-0001 dans l'image api:latest", "horodatage": "2026-01-01T17:00:04"},
    {"source": "prometheus", "type": "alerte", "severite": "info",
     "message": "CPU a 40%", "horodatage": "2026-01-01T17:00:05"},
]

if __name__ == "__main__":
    executer(DEMO)
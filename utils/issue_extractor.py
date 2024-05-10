import os
import pdb
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_issues(review_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Identifizier und list die häufigen negativen Themen aus der folgenden App-Store-Bewertung auf. Nutz konkrete standardisierte Begriffe wie 'Störungsmeldung'. Trenn jedes Problem mit einem Komma.: '{}'. ".format(
                        review_text
                    ),
                }
            ],
            max_tokens=100,
            temperature=0.3,
        )
        pdb.set_trace()
        issues = response.choices[0].message.content.strip()
        return [issue.strip() for issue in issues.split(",")]
    except Exception as e:
        print(f"Error processing review: {e}")
        return []


extract_issues(
    """
    Nach dem Relauch der App hat sich ihre Qualität extrem verschlechtert. Die App ist extrem unübersichtlich, vieles nicht oder nur schwer zu finden. In manchen Teilen wird einfach auf eine Webseite verlinkt – warum die Funktion nicht einfach in der App spiegeln?
    In manchen Teilen wird der halbe Bildschirm durch ein statisches Fenster verdeckt und es bleibt nur eingeschränkt der Bereich und den Informationstext zu scrollen.
    Eine Störungsmeldung zu einem defekten Ampelanlage hat nur ein sehr kleines, einzeiliges Feld für eine Anmerkung, obwohl der halbe Bildschirm frei ist. Anstatt die Meldung aus der App zu versenden wird eine Mail für mein Mail Programm generiert.
    Meine Daten zu Ermittlung von Zähler ständen wurden mit dem Update gelöscht und ich muss mich komplett neu anmelden. Ob allem auch meine vorherigen Erfassung verschwunden sind bleibt unklar.
    Ich frag mich echt wie man eine App durch einen Relaunch so sehr verschlechtern kann.
    """
)

# PROMPT NEEDS WORK!
# (Pdb) response.choices[0].message.content.strip()
# 'Unübersichtlichkeit, Verlinkung auf Webseite, Statisches Fenster verdeckt Bildschirm, Einschränktes Scrollen, Kleines Feld für Störungsmeldung, Mail statt App-Versand, Daten gelöscht nach Update, Neuanmeldung erforderlich, Verlust vorheriger Erfassungen, Verschlechterung durch Relaunch.'

![EM Logo](em_model_logo_web.jpeg)

([English Version](README.md))

# Inhalt

- [Einleitung](#einleitung)
- [Download und & Demos](#links--demos)
  - [Model Links](#model-links)
  - [Colab](#colab)
- [Eingabeformat](#eingabeformat)
- [Ergebnisse](#ergebnisse)
  - [Beispiel-Ausgaben](#beispiel-ausgaben)
  - [Sachliche Abfrage / RAG](#sachliche-abfrage--rag)
  - [Evaluation](#evaluation)
- [Datensatz](#datensatz)
- [Danksagungen](#danksagungen)
- [Kontakt](#kontakt)
- [Haftungsausschluss](#haftungsausschluss)

# Einleitung

**EM German (v01)** ist eine experimentelle, Llama2-basierte KI-Modellreihe, die in deutscher Sprache fine-getuned wurde. 

Die Modelle sind für deutschen Text optimiert und können Inhalte in deutscher Sprache verstehen und generieren. Alle Modelle stehen frei zum kostenlosen Download zur Verfügung und können lokal und ohne Internetzugriff genutzt werden.

# Download & Demo

Anbei finden sich die Links für die einzelnen Modelle zum Download. Sollten Sie keine Programmierkenntnisse haben und Ihnen die verschiedenen Modelle nichts sagen, folgen Sie am besten [dieser Anleitung](examples/LM_Studio/Anleitung.md) für eine lokale Installation mit grafischer Benutzeroberfläche.

## Model Links

Sollten Sie nur ein Modell ausprobieren, empfehle ich stark das **LeoLM Mistral** Modell, was mit Abstand die beste Kombination von Performance und Ressourcenanforderungen bietet!

| Base Model | HF    | GPTQ  | GGUF  | AWQ   |
|-------|-------|-------|-------|-------|
| Llama2 7b   | [Link](https://huggingface.co/jphme/em_german_7b_v01) | [Link](https://huggingface.co/TheBloke/em_german_7b_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_7b_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_7b_v01-AWQ) |
| Llama2 13b  | [Link](https://huggingface.co/jphme/em_german_13b_v01) | [Link](https://huggingface.co/TheBloke/em_german_13b_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_13b_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_13b_v01-AWQ) |
| Llama2 70b   | [Link](https://huggingface.co/jphme/em_german_70b_v01) | [Link](https://huggingface.co/TheBloke/em_german_70b_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_70b_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_70b_v01-AWQ) |
| [Mistral 7b](https://huggingface.co/mistralai/Mistral-7B-v0.1) | [Link](https://huggingface.co/jphme/em_german_mistral_v01) | [Link](https://huggingface.co/TheBloke/em_german_mistral_v01-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_mistral_v01-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_mistral_v01-AWQ) |
| [LeoLM 7b](https://huggingface.co/LeoLM/leo-hessianai-7b) | [Link](https://huggingface.co/jphme/em_german_7b_leo) | [Link](https://huggingface.co/jphme/em_german_7b_leo_gptq) | [Link](hhttps://huggingface.co/jphme/em_german_7b_leo_gguf) | tbc |
| [LeoLM 13b](https://huggingface.co/LeoLM/leo-hessianai-13b) | soon | soon | [Link](https://huggingface.co/jphme/em_german_13b_leo_gguf) | tbc |
| [LeoLM Mistral](https://huggingface.co/LeoLM/leo-mistral-hessianai-7b) | [Link](https://huggingface.co/jphme/em_german_leo_mistral) | [Link](https://huggingface.co/TheBloke/em_german_leo_mistral-GPTQ) | [Link](https://huggingface.co/TheBloke/em_german_leo_mistral-GGUF) | [Link](https://huggingface.co/TheBloke/em_german_leo_mistral-AWQ) |

### Hinweise zu den Modellversionen
Grundsätzlich empfehle ich die **Leo Mistral* Variante. Für einen Vergleich der verschiedenen (7b) Versionen anhand Beispielprompts, siehe [hier](example_output_comparison.md).

## Grafische Benutzeroberfläche
Anbei Anleitungen/Links für eine Nutzung der EM German Modelle mit grafischer Benutzeroberfläche:
### LM Studio

Eine Anleitung zur Nutzung auf dem eigenen Rechner (Windows/Mac) mit LM Studio findet sich [hier](examples/LM_Studio/Anleitung.md).

### GPT4All

EM German Mistral (non-LeoLM) wird ab Version 2.5 (derzeit im pre-release) auch offiztiell von [GPT4All](https://gpt4all.io/index.html) unterstützt.
Die pre-release Version kann man hier downloaden:
* [Windows](https://gpt4all.io/installers_offline/gpt4all-installer-win64-v2.5.0-pre1.exe)
* [MacOS](https://gpt4all.io/installers_offline/gpt4all-installer-darwin-v2.5.0-pre1.dmg)
* [Linux](https://gpt4all.io/installers_offline/gpt4all-installer-linux-v2.5.0-pre1.run)


## Colab:

Einige der Modelle können mit kostenlosen Google Colab-Instanzen verwendet werden (z.B. das 7b-Modell in 8-Bit oder das 13b-Modell mit GPTQ):

* [Beispiel-Notebook 13b mit GPTQ](https://colab.research.google.com/drive/1IJfJdVwGkfe5MYOqHptystR3FBeEUdGn?usp=sharing)
* [Beispiel-Notebook 7b mit 8-Bit](https://colab.research.google.com/drive/1bsv6vkLM4AlCpSyXA6ol9P32zxZmf7Zu?usp=sharing)
* [Beispiel-Notebook 7b Mistral GGUF mit Grammar-based structured Output](https://colab.research.google.com/drive/17O-a3D4BnVc_V9Of3dFfed18v1ULu1Sv?usp=sharing)

# Eingabeformat

Dieses Modell folgt dem sogennanten "Vicuna-Format" ohne Zeilenumbrüche (sollte aber auch mit Zeilenumbrüchen funktionieren). Das Format lautet wie folgt:

```
Du bist ein hilfreicher Assistent. USER: <Anweisung> ASSISTANT:
```

Sie können das Standard-Systemprompt aber auch ändern (siehe unten für ein Beispiel bei Aufgaben mit externen Datenbanken).

# Ergebnisse

Anbei einige Beispiele für Modell-Outputs. Wir werden demnächst einige kleine deutsche Benchmarks veröffentlichen (basierend auf dem Eleuther LM Evaluation Harness), die wir bei diesen Modellen bereits getstet haben.
Mehr Beispiele und Vergleiche zwischen den verschiedenen Modell-Versionen finden Sie [hier](example_output_comparison.md). 

## Beispiel-Ausgaben

Prompt:
```
Du bist ein hilfreicher Assistent USER: Ein Buch hat 500 Seiten. Jede Seite enthält 300 Wörter. Wie viele Wörter sind im gesamten Buch enthalten? ASSISTANT:
```

Antwort EM 7b v01
```
Die Gesamtzahl der Wörter in dem Buch kann berechnet werden, indem man die Anzahl der Wörter pro Seite mit der Gesamtzahl der Seiten multipliziert.

Gesamtzahl der Wörter = Anzahl der Wörter pro Seite * Gesamtzahl der Seiten = 300 Wörter pro Seite * 500 Seiten = 150.000 Wörter

Das Buch enthält also insgesamt 150.000 Wörter.
```

Prompt:
```
Du bist ein hilfreicher Assistent USER: Erläutere die Grundprinzipien der evolutionären Biologie und Genetik, indem du den Prozess der natürlichen Selektion, die Rolle von Mutationen und genetischer Drift sowie das Konzept der adaptiven Radiation erklärst. ASSISTANT:
```

Antwort EM 7b v01:
```
Die Evolutionäre Biologie und Genetik sind zwei intim verwandte Disziplinen, die sich mit dem Studium des Verhaltens und der Entwicklung von Organismen in der Natur befassen. Sie untersuchen, wie Arten sich im Laufe der Zeit entwickeln und wie diese Veränderungen genetisch bedingt sind.

    1. Natürliche Selektion: Die natürliche Selektion ist ein grundlegendes Prinzip in der Evolutionäre Biologie. Es besagt, dass Individuen innerhalb einer Spezies unterschiedliche Fähigkeiten oder Merkmale aufweisen können. Diese Merkmale beeinflussen ihre Überlebens- und Fortpflanzungsrate. Diejenigen mit Vorteilen haben eine höhere Wahrscheinlichkeit, ihre Gene an zukünftige Generationen weiterzugeben und so die Art im Laufe der Zeit zu verändern.

    2. Rolle von Mutationen: Mutationen sind Veränderungen im Genom eines Organismus, die entweder durch zufällige Fehler während der Replikation oder durch Exposition gegenüber Strahlung verursacht werden. Diese Veränderungen können dazu führen, dass ein Individuum neue Eigenschaften aufweist, die es im Kampf ums Überleben vorteilhaft machen könnten. Diese Mutationen werden dann von der natürlichen Selektion beeinflusst und können so zur Entwicklung neuer Arten beitragen.

    3. Genetische Drift: Genetische Drift ist ein zufälliger Prozess, der durch die Verteilung von Allelen in einer Population stattfindet. Wenn eine Population kleiner wird oder wenn die Überlebens- und Fortpflanzungsraten zwischen den Individuen variieren, kann dies dazu führen, dass bestimmte Gene stärker oder weniger häufig werden. Dies kann dazu führen, dass die Population im Laufe der Zeit unterschiedliche Merkmale aufweist.

    4. Adaptive Radiation: Adaptive Radiation ist ein Prozess, bei dem eine Art mehrere verschiedene Linien auslässt, die sich auf verschiedene Weise an ihre Umgebung anpassen. Dies geschieht normalerweise, wenn die Umwelt sich ändert und die Art neue Fähigkeiten benötigt, um überleben zu können. Die verschiedenen Linien können dann unterschiedliche Eigenschaften entwickeln, die ihnen helfen, in dieser neuen Umgebung zu überleben.
```

## Beispiel für grammar-based structured Output mit GGUF

Prompt:
> "Max ging im Jahr, als die Corona-Krise startete, in die Stadt mit dem Eiffelturm."

EM German Mistral 7b GGUF Q8_0:
```python
{'jahr': 2020, 'name': 'Paris', 'ort': 'Frankreich'}
```
(siehe [Beispiel Notebook](https://colab.research.google.com/drive/17O-a3D4BnVc_V9Of3dFfed18v1ULu1Sv?usp=sharing) für details).

## Sachliche Abfrage / RAG

EM-Modelle bieten ein spezielles Format für RAG (also die Verwendung mit Informationen aus zusätzlichen externen Quellen wie Datenbanken oder Websiten), das für die Minimierung von Halluzinationen und Falscinformationen optimiert ist. Wir verwenden dasselbe Format wie Airoboros dafür.

### Beispiel

Prompt
```
Du bist ein hilfreicher Assistent. Für die folgende Aufgabe stehen dir zwischen den tags BEGININPUT und ENDINPUT mehrere Quellen zur Verfügung. Metadaten zu den einzelnen Quellen wie Autor, URL o.ä. sind zwischen BEGINCONTEXT und ENDCONTEXT zu finden, danach folgt der Text der Quelle. Die eigentliche Aufgabe oder Frage ist zwischen BEGININSTRUCTION und ENDINCSTRUCTION zu finden. Beantworte diese wortwörtlich mit einem Zitat aus den Quellen. Sollten diese keine Antwort enthalten, antworte, dass auf Basis der gegebenen Informationen keine Antwort möglich ist! USER: BEGININPUT
BEGINCONTEXT
Url: https://www.jph.me
ENDCONTEXT 
Das Wetter in Düsseldorf wird heute schön und sonnig!
ENDINPUT
BEGININSTRUCTION Was ist 1+1? ENDINSTRUCTION ASSISTANT:
```

Modellantwort:
```
Mit den gegebenen Informationen ist diese Frage nicht zu beantworten.
```

Hier würde das Modell normalerweise die (triviale) Antwort (2) geben, ist aber trainiert, keine Antwort zu geben, wenn es keine Quelle zwischen BEGININPUT und ENDINPUT gibt, die eine belegbare Antwort liefert.

Wenn wir anstattdessen fragen:
```
BEGININSTRUCTION Wie wird das Wetter heute in Düsseldorf? Gebe die Quelle mit an! ENDINSTRUCTION ASSISTANT:
```

Bekommen wir die korrekte Antwort mit Quellenangabe

```
Das Wetter in Düsseldorf wird heute schön und sonnig! (Quelle: Url: https://www.jph.me)
```
# Evaluation

coming soon

# Datensatz

Der Datensatz ist eine Mischung aus Multi-Turn-Chats, RAG Instructions und synthetisch generierten Finetuning-Daten, die viele Themen und Anwendungen abdecken.


# Danksagungen:

Vielen Dank an [winglian](https://huggingface.co/winglian) für seine großartige Arbeit an Axolotl, die ich zur Schulung der EM-Modelle verwendet habe. Ich bin auch [Jon Durbin](https://huggingface.co/jondurbin) für seine Arioboros Modelle und Code-Schnipsel dankbar, von denen ich viele Ideen nutzen konnte.
Vielen Dank außerdem an [Björn Plüster](https://huggingface.co/bjoernp) und das LeoLM Team für das hervorragende LeoLM-Modell und natürlich an [TheBloke](https://huggingface.co/TheBloke) für die Bereitstellung der quantisierten Modelle in allen erdenklichen Formaten.
Das 70b-Modell wurde mit Unterstützung des [OVH Cloud Startup Program](https://startup.ovhcloud.com/en/) trainiert.

# Kontakt

Wenn Sie an customized LLMs für geschäftliche Anwendungen interessiert sind, kontaktieren Sie mich bitte über [meine Website](https://www.jph.me). Ich freue mich auch immer über Anregungen und Feedback zu meinen Modellen.

*PS: Ich suche auch immer noch Mitstreiter für unser Startup ellamind, das kommerzielle Lösungen zur Prozessautomatisierung auf Basis von LLMs anbieten wird (Derzeit noch im Stealth-Modus).*

# Haftungsausschluss:

Ich bin nicht verantwortlich für die Handlungen Dritter, die dieses Modell verwenden. Dieses Modell sollte nur für Forschungszwecke verwendet werden. Die ursprüngliche Llama2-Lizenz gilt und wird mit den Modell-Dateien verteilt.
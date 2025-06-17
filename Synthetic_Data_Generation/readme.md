# Synthetic Data Generation with Large Language Models (Google Colab)

Generate high‑quality synthetic **financial sentiment data** using the Mixtral‑8x7B‑Instruct model served via the Hugging Face Inference API. The workflow downloads the **Financial PhraseBank** corpus, auto‑labels each sentence, and writes a ready‑to‑train CSV.

---

## Key Features

| Feature                       | What it does                                                                                          |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Plug‑and‑play notebook**    | A single Colab notebook handles dataset download, prompting, generation, post‑processing and metrics. |
| **Self‑Consistency Decoding** | Runs *n* parallel generations per example and chooses the majority label for robustness.              |
| **Zero‑Cost Training Data**   | No manual annotation needed—ideal for bootstrapping models or augmenting small corpora.               |
| **Configurable**              | Tweak model, prompt, seed, sample size, temperature, etc. from the notebook header.                   |

---

##  Project Structure

```
├── synthetic_data_generation_colab.ipynb  # Main Colab notebook
├── df_train.csv                           # Resulting synthetic dataset (created after running)
├── .env.example                           # Template for environment variables
└── README.md                              # You are here
```

---

## 🚀 Quick Start in Google Colab

### 1. Open in Google Colab

Click the button below to open the notebook in Colab:



### 2. Setup Environment

The notebook will install all dependencies automatically:

```python
!pip install --upgrade pip -q
!pip install transformers~=4.37.2 huggingface_hub~=0.20.3 datasets~=2.16.1 openai~=1.11.0 scikit-learn pandas tqdm python-dotenv
```

### 3. Configure Hugging Face Token

1. Create a Hugging Face account
2. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and create a token
3. Run `huggingface_hub.login()` in a cell and paste your token when prompted

### 4. Run All Cells

Execute the notebook from top to bottom. A CSV named `df_train.csv` will be saved with the generated labels.

---

## ⚙️ Configuration

Adjust these globals at the top of the notebook:

| Variable                      | Purpose                          | Example                                                                            |
| ----------------------------- | -------------------------------- | ---------------------------------------------------------------------------------- |
| `API_URL`                     | Endpoint of the inference model  | `https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1` |
| `SEED`                        | RNG seed for reproducibility     | `42`                                                                               |
| `N_SAMPLE`                    | Sample size for quick dry‑runs   | `100` or `False` for full set                                                      |
| `SELF_CONSISTENCY_ITERATIONS` | How many generations per example | `3`                                                                                |
| `DATA_SUBSET`                 | Financial PhraseBank variant     | `sentences_allagree`                                                               |

---

## 📊 Output

`df_train.csv` columns:

| column   | description                                               |
| -------- | --------------------------------------------------------- |
| `text`   | Original sentence from Financial PhraseBank               |
| `labels` | Predicted sentiment (`positive` / `negative` / `neutral`) |

---

## 📝 References

- Malo et al., **"Financial PhraseBank for Sentiment Analysis"** (2014) – original dataset paper.
- Hugging Face Inference API – [https://huggingface.co/inference-api](https://huggingface.co/inference-api).

---

## 🛡️ License

This repository is licensed under the **Apache 2.0** License. The Financial PhraseBank dataset is distributed under its own research license—see the dataset card for details.

---

## 🙋‍♂️ Questions / Help

Open an issue or start a discussion on the repo if you get stuck. PRs welcome!



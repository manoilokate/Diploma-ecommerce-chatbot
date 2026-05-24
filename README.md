# 🤖 Чат-бот для електронної комерції на основі донавчених LLM

> *Дослідження та порівняння двох компактних мовних моделей (Qwen2.5-1.5B та Llama-3.2-1B) як основи для чат-бота онлайн-магазину одягу з підтримкою механізму function calling.*

---

## 👤 Автор

- **ПІБ**: Манойло Катерина Сергіївна
- **Група**: ФеІ-42с
- **Керівник**: Гусак Олег Васильович, асистент кафедри системного проектування
- **Дата виконання**: 24.05.2026

---

## 📌 Загальна інформація

- **Тип проєкту**: Дослідницька кваліфікаційна робота з прикладною реалізацією (Jupyter Notebooks + Gradio-інтерфейс)
- **Мова програмування**: Python 3.10+
- **Фреймворки / Бібліотеки**: Unsloth, HuggingFace Transformers, TRL, PyTorch, bitsandbytes, Gradio, sentence-transformers, rouge-score, bert-score, NLTK, matplotlib

---

## 🧠 Опис функціоналу

- 🎯 Донавчання двох відкритих LLM-моделей (Qwen2.5-1.5B-Instruct та Llama-3.2-1B-Instruct) методом LoRA з 4-бітною квантизацією (QLoRA)
- 📚 Власний синтетично-згенерований датасет з 12 000 діалогів для навчання function calling
- 🛒 Емулятор інтернет-магазину з 12 функціями бекенду (пошук, перевірка наявності, оформлення замовлення, оплата, доставка, відстеження, скасування, оновлення, повернення)
- 🔀 Рушій діалогу з підтримкою трьох режимів роботи: Pure LLM, шаблони відповідей (Templates), скінченний автомат (State Machine)
- 📊 Комплексна методологія тестування з 62 тестових сценаріїв та зважений рейтинг моделей
- 🖥️ Демонстраційний інтерфейс на Gradio з паралельним порівнянням двох моделей у режимі реального часу

---

## 🧱 Опис основних файлів

| Файл                                    | Призначення                                                     |
|-----------------------------------------|-----------------------------------------------------------------|
| `diploma-model-training.ipynb`          | Донавчання моделей Qwen та Llama методом LoRA на Kaggle         |
| `diploma-model-comparison.ipynb`        | Комплексне тестування донавчених моделей за 62 сценаріями       |
| `diploma-demo.ipynb`                    | Демонстраційний інтерфейс на Gradio з трьома режимами роботи    |
| `ecommerce_function_calling_12000.json` | Власний синтетичний датасет з прикладами викликів функцій       |
| `dataset_generation.py`                 | Скрипт генерації синтетичного датасету                          |
| `plot_loss.py`                          | Побудова графіків кривих втрат для обох моделей                 |

---

## ▶️ Як запустити проєкт «з нуля»

### 1. Встановлення інструментів

- Python 3.10 або новіший
- CUDA-сумісний GPU (для тренування — мінімум 15 GB VRAM, наприклад Tesla T4)
- Обліковий запис на HuggingFace для завантаження моделей
- Обліковий запис на Kaggle (рекомендовано для безкоштовного GPU)

### 2. Клонування репозиторію

```bash
git clone https://github.com/manoilokate/diploma-ecommerce-chatbot.git
cd diploma-ecommerce-chatbot
```

### 3. Встановлення залежностей

```bash
pip install "unsloth[kaggle-new] @ git+https://github.com/unslothai/unsloth.git"
pip install "transformers==5.3.0" "trl>=0.18.2,<=0.24.0,!=0.19.0"
pip install rouge-score bert-score nltk sentence-transformers
pip install gradio matplotlib pandas
```

### 4. Налаштування токенів HuggingFace

Створити секрети у Kaggle або змінні середовища:

```
HF_TOKEN=hf_xxxxxxxxxxxxxxx        # для завантаження моделей
DiplomaWrite=hf_xxxxxxxxxxxxxxx    # для завантаження донавчених моделей на Hub
```

### 5. Запуск

```bash
# Тренування моделей (на Kaggle з GPU Tesla T4)
jupyter notebook diploma-qwen2-7b-training.ipynb

# Порівняльне тестування донавчених моделей
jupyter notebook diploma-model-comparison.ipynb

# Демонстраційний інтерфейс
jupyter notebook diploma-demo.ipynb
```

---

## 🛒 Функції бекенду емулятора

### 🔍 Пошук та вибір товару

**`search_products(category, color?)`** — пошук товарів у каталозі за категорією та опціонально кольором.

```json
{"name": "search_products", "arguments": {"category": "dresses", "color": "Black"}}
```

**`check_product_availability(product_name, color, size)`** — перевірка наявності конкретного товару на складі.

```json
{"name": "check_product_availability", "arguments": {"product_name": "Luna", "color": "Black", "size": "M"}}
```

### 📝 Оформлення замовлення

**`create_order(product_name, color, size, quantity)`** — створення нового замовлення зі статусом draft.

**`confirm_payment(payment_method)`** — підтвердження способу оплати (card / cash).

**`add_delivery_details(name, phone, city, post_office)`** — додавання даних доставки.

**`confirm_order()`** — фінальне підтвердження оформленого замовлення.

### 📦 Управління замовленнями

**`track_order(order_id)`** — відстеження статусу замовлення.

**`cancel_order(order_id)`** — скасування замовлення.

**`update_order_item(order_id, field, new_value)`** — оновлення параметрів замовлення (розмір або колір).

**`create_return_request(order_id, reason)`** — оформлення запиту на повернення.

### ℹ️ Допоміжні функції

**`get_current_order_context()`** — отримання активних замовлень поточного клієнта.

**`get_order_history(limit)`** — історія замовлень клієнта.

---

## 🖱️ Інструкція для користувача

1. **Запуск демонстраційного інтерфейсу** — після запуску `diploma-demo.ipynb` відкривається веб-сторінка з двома паралельними чатами (Qwen та Llama).

2. **Налаштування експерименту** у верхній панелі:
   - `👤 Customer profile` — вибір тестового профілю або «New Customer»
   - `🔀 Response mode` — Model response (raw) / Formatted (template)
   - `🔀 State machine` — увімкнути/вимкнути скінченний автомат

3. **Спілкування з ботом**:
   - `Send both` — надсилання повідомлення одночасно обом моделям для порівняння
   - Окремі поля «Message to Qwen only…» / «Message to Llama only…» — надсилання тільки одній моделі
   - `Clear` — очищення історії обох діалогів

4. **Тестові сценарії** — у розділі Sample prompts є готові приклади запитів за категоріями: пошук, оформлення замовлення, доставка, відстеження, скасування, повернення, історія.

5. **Спостереження за роботою системи**:
   - Хедер чату — час відповіді, токени за секунду, викликана функція
   - Function calls — журнал викликів функцій з параметрами та результатами
   - Database snapshot — поточний стан бази даних емулятора

---

## 📷 Приклади / скриншоти

- Загальний вигляд демонстраційного інтерфейсу
- Готові приклади запитів (Sample prompts)
- Панель бази даних емулятора (Database snapshot)
- Поведінка моделей у чотирьох конфігураціях (Pure LLM, +Templates, +State Machine, +Both)

(скріни наведено у пояснювальній записці)

---

## 🧪 Проблеми і рішення

| Проблема                                  | Рішення                                                                               |
|-------------------------------------------|---------------------------------------------------------------------------------------|
| Out of memory при тренуванні              | Зменшити `per_device_train_batch_size` до 1 і збільшити `gradient_accumulation_steps` |
| Модель галюцинує назви функцій            | Перетренувати з більшим `max_seq_length` (1024/2048 замість 512)                      |
| Помилка завантаження моделі з HuggingFace | Перевірити коректність HF_TOKEN та доступність моделі                                 |
| Демо «зависає» при першому запуску        | Зачекати завантаження моделей (~1-2 хв на Tesla T4)                                   |
| Старий стан БД після оновлення схеми      | Видалити файл `demo_db.json` для перезапуску з дефолтними даними                      |

---

## 🧾 Використані джерела / література

- Average e-commerce spending per online shopper worldwide per visit in the 4th quarter of 2025, by category — statista.com/statistics/239288/countries-ranked-by-average-b2c-e-commerce-spending-per-online-buyer
- Vaswani et al., "Attention Is All You Need", NeurIPS 2017 — proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
- Qwen Team, "Qwen2.5: A Party of Foundation Models" — qwen.ai/blog?id=qwen2.5
- Qwen2.5-1.5B-Instruct — huggingface.co/Qwen/Qwen2.5-1.5B-Instruct
- Meta AI, "Llama 3.2: Revolutionizing edge AI and vision with open, customizable models" — ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices
- Llama-3.2-1B-Instruct — huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", arXiv:2106.09685
- Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs", arXiv:2305.14314
- Unsloth Documentation — unsloth.ai/docs/basics/api
- HuggingFace TRL, SFT Trainer — huggingface.co/docs/trl/sft_trainer
- Bitext Customer Support LLM Chatbot Training Dataset — huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset
- ToolBench — github.com/OpenBMB/ToolBench
- Salesforce, xLAM-60k — huggingface.co/datasets/Salesforce/xlam-function-calling-60k
- Xu et al., "A Survey on Knowledge Distillation of Large Language Models", arXiv:2402.13116
- Dettmers et al., "8-bit Optimizers via Block-wise Quantization", arXiv:2110.02861
- Wang et al., "A Survey on Large Language Model based Autonomous Agents", arXiv:2308.11432

---
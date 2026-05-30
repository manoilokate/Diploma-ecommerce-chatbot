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

- Обліковий запис на [Kaggle](https://www.kaggle.com) — для запуску всіх ноутбуків з безкоштовним GPU Tesla T4
- Обліковий запис на [HuggingFace](https://huggingface.co) — для зчитування моделей та завантаження донавчених версій

### 2. Клонування репозиторію

```bash
git clone https://github.com/manoilokate/Diploma-ecommerce-chatbot.git
cd Diploma-ecommerce-chatbot
```

### 3. Завантаження файлів у Kaggle

1. Зайти на [kaggle.com](https://www.kaggle.com) → `Code` → `New Notebook`
2. У відкритому ноутбуці натиснути `File` (верхній лівий кут) → `Import Notebook` → вибрати файл з локального репозиторію:
   - спочатку завантажити `diploma-model-training.ipynb`
   - потім аналогічно — `diploma-model-comparison.ipynb` та `diploma-demo.ipynb`
3. Завантажити датасет як окремий ресурс Kaggle:
   - перейти на [kaggle.com/datasets](https://www.kaggle.com/datasets) → `New Dataset`
   - завантажити файл `ecommerce_function_calling_12000.json` → назвати датасет `ecommerce-function-calling-12000` → `Create`
   - у ноутбуці натиснути `+ Add Input` (права панель) → `Datasets` → знайти щойно створений датасет і додати його
4. Увімкнути GPU у налаштуваннях ноутбука: верхня панель → `Settings` → `Accelerator → GPU T4 x2` 

### 4. Налаштування токенів HuggingFace

**Крок 4.1 — Створити токени на HuggingFace:**

1. Зайти на [huggingface.co](https://huggingface.co) → `Profile` → `Settings` → `Access Tokens` → `New token`
2. Створити **перший токен** (`HF_TOKEN`):
   - Name: `HF_TOKEN`
   - Role: `Read` (достатньо для завантаження моделей)
   - Натиснути `Generate token` → скопіювати значення
3. Створити **другий токен** (`DiplomaWrite`):
   - Name: `DiplomaWrite`
   - Role: `Write` (потрібен для завантаження донавчених моделей на Hub)
   - Натиснути `Generate token` → скопіювати значення

**Крок 4.2 — Додати токени у Kaggle Secrets:**

1. У Kaggle Notebook натиснути `Add-ons` (верхнє меню) → `Secrets`
2. Натиснути `Add a new secret` і додати два записи:

```
Name: HF_TOKEN        Value: hf_xxxxxxxxxxxxxxx
Name: DiplomaWrite    Value: hf_xxxxxxxxxxxxxxx
```

3. Для кожного секрету увімкнути перемикач `Attach to notebook`

### 5. Запуск

Послідовно запускати ноутбуки у Kaggle — усі необхідні залежності встановлюються автоматично у першій клітинці кожного ноутбука.

Для кожного ноутбука:
1. Відкрити ноутбук у Kaggle
2. Переконатись, що GPU увімкнено: верхня панель → `Settings` → `Accelerator → GPU T4 x2`
3. Натиснути `Run All` (`▶▶` або `Run` → `Run All`) — Kaggle запустить усі клітинки послідовно

**Порядок запуску:**

1. `diploma-model-training.ipynb` — донавчання моделей (~6–8 годин на одну модель з 3 епохами на GPU Tesla T4); після завершення донавчені моделі автоматично зберігаються на HuggingFace Hub
2. `diploma-model-comparison.ipynb` — тестування донавчених моделей за 62 сценаріями (~30 хвилин)
3. `diploma-demo.ipynb` — запускає Gradio-інтерфейс; у виводі останньої клітинки з'явиться публічне посилання виду `https://xxxx.gradio.live` — відкрити його у браузері

**Побудова графіків втрат (локально):**

`plot_loss.py` запускається локально на вашому комп'ютері — дані втрат вже вшиті у скрипт як константи (результати реального тренування). Потребує лише встановленого `matplotlib`:

```bash
pip install matplotlib
python plot_loss.py
```

Результат зберігається у файл `loss_curves.png` у поточній папці.

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

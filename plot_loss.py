import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ── Llama-3.2-1B data ─────────────────────────────────────
llama_steps = [
    300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000,
    3300, 3600, 3900, 4200, 4500, 4800, 5100, 5400, 5700, 6000,
    6300, 6600, 6900, 7200, 7500, 7800, 8100, 8400, 8700, 9000,
    9300, 9600, 9900, 10200
]
llama_train = [
    0.549150, 0.497347, 0.450509, 0.450333, 0.433134, 0.415418, 0.424379,
    0.433713, 0.407914, 0.432510, 0.418451, 0.378788, 0.384950, 0.388688,
    0.386254, 0.382411, 0.374816, 0.368800, 0.370602, 0.379665, 0.360230,
    0.355883, 0.365188, 0.324556, 0.337988, 0.332221, 0.323881, 0.329689,
    0.327536, 0.323837, 0.313863, 0.329017, 0.333311, 0.315577
]
llama_val = [
    0.546376, 0.494414, 0.471199, 0.458948, 0.450525, 0.443345, 0.435966,
    0.431593, 0.429543, 0.423470, 0.419079, 0.419389, 0.415507, 0.414018,
    0.411422, 0.408801, 0.406120, 0.404115, 0.401488, 0.399856, 0.396362,
    0.393831, 0.392632, 0.395914, 0.395657, 0.393477, 0.393498, 0.392034,
    0.391143, 0.390911, 0.390522, 0.390038, 0.389993, 0.389963
]

# ── Qwen2.5-1.5B data ─────────────────────────────────────
qwen_steps = [
    300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000,
    3300, 3600, 3900, 4200, 4500, 4800, 5100, 5400, 5700, 6000,
    6300, 6600, 6900
]
qwen_train = [
    0.586463, 0.539096, 0.496561, 0.470764, 0.490613, 0.486674, 0.472892,
    0.479286, 0.446937, 0.473193, 0.470794, 0.429732, 0.409398, 0.410507,
    0.418514, 0.422845, 0.420051, 0.411850, 0.419822, 0.415374, 0.402846,
    0.404061, 0.383605
]
qwen_val = [
    0.598381, 0.544440, 0.520935, 0.506135, 0.497198, 0.487340, 0.482388,
    0.477856, 0.472445, 0.468633, 0.464397, 0.462989, 0.460000, 0.459544,
    0.454961, 0.453062, 0.449767, 0.447097, 0.444271, 0.442559, 0.439962,
    0.438194, 0.440402
]

# ── Plot ───────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Training Dynamics", fontsize=15, fontweight="bold", y=1.02)

colors = {
    "llama_train": "#2196F3",
    "llama_val":   "#0D47A1",
    "qwen_train":  "#FF7043",
    "qwen_val":    "#BF360C",
}

# — Llama subplot —
ax = axes[0]
ax.plot(llama_steps, llama_train, color=colors["llama_train"],
        linewidth=1.8, label="Train loss", alpha=0.85)
ax.plot(llama_steps, llama_val,   color=colors["llama_val"],
        linewidth=2.0, label="Validation loss", linestyle="--")
ax.set_title("Llama-3.2-1B-Instruct", fontsize=12, fontweight="bold")
ax.set_xlabel("Step")
ax.set_ylabel("Loss")
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.4)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.3f"))
ax.set_xlim(left=0)

# — Qwen subplot —
ax = axes[1]
ax.plot(qwen_steps, qwen_train, color=colors["qwen_train"],
        linewidth=1.8, label="Train loss", alpha=0.85)
ax.plot(qwen_steps, qwen_val,   color=colors["qwen_val"],
        linewidth=2.0, label="Validation loss", linestyle="--")
ax.set_title("Qwen2.5-1.5B-Instruct", fontsize=12, fontweight="bold")
ax.set_xlabel("Step")
ax.set_ylabel("Loss")
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.4)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.3f"))
ax.set_xlim(left=0)

plt.tight_layout()
plt.savefig("C:/44year/Diploma/loss_curves.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: loss_curves.png")

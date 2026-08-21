# Titanic EDA — Stakeholder Insight Summary

## Executive Takeaway

**Survival was strongly associated with passenger class and gender, while family size showed a non-linear relationship with survival.** The clearest pattern was the combination of gender and class: first-class females had a **96.8%** survival rate, compared with only **13.5%** for third-class males.

## Three Key Insights

### 1. Gender mattered, but passenger class changed the size of the difference

Female passengers had higher survival rates than males in every class, but survival also changed substantially within each gender:

| Passenger Group | Survival Rate |
|---|---:|
| 1st-class female | **96.8%** |
| 2nd-class female | **92.1%** |
| 3rd-class female | **50.0%** |
| 1st-class male | **36.9%** |
| 2nd-class male | **15.7%** |
| 3rd-class male | **13.5%** |

**What this means:** Looking at gender or class alone misses an important part of the pattern. The combination of the two variables separated passengers into very different survival groups.

### 2. Small family groups had the best outcomes

Survival was not simply higher or lower as family size increased.

- **Small family groups:** ~58% survival
- **Traveling alone:** ~30% survival
- **Large family groups:** ~16% survival

**What this means:** Traveling with a small family group was associated with better survival outcomes, while very large family groups had substantially lower survival. Grouping family sizes also reduces the influence of extremely small categories such as family sizes 8 and 11.

### 3. Passenger class remained important across age groups

When age was divided into children, teens, adults, middle-aged passengers, and seniors, passenger class continued to show a strong association with survival. First-class passengers generally had higher survival rates than lower-class passengers across comparable age groups.

Some subgroup results should be treated cautiously. For example, **2nd-class children had a 100% survival rate, but this was based on only 17 passengers**.

**What this means:** Age alone does not explain the survival pattern; passenger class remains an important factor when age is considered.

## What Can We Trust?

The strongest conclusions are the patterns that remain visible across multiple comparisons, particularly the relationship between **passenger class, gender, and survival**. The family-size pattern is also clearer after combining individual family sizes into broader groups.

These findings describe **associations**, not causes. Small subgroups can produce unstable survival rates, so individual percentages should not be generalized without considering sample size.

## Data Quality & Modeling Risks

- **Target leakage:** `Survived` is the outcome being predicted and must not be included as a model feature.
- **Identifier risk:** `PassengerId` identifies a passenger but does not represent a meaningful passenger characteristic and should generally be excluded from modeling.
- **High Cabin missingness:** Approximately **77% of Cabin values were missing** in the raw data, limiting how reliably cabin-related patterns can be analyzed.
- **Age imputation:** Missing `Age` values were filled using the median. This preserves records but reduces variation and may influence model results.
- **Small subgroups:** Some age/class combinations contain few observations, making their survival rates less reliable.

## Conclusion

The analysis suggests that **who a passenger was and the class in which they traveled were closely associated with survival**. The most pronounced difference was between first-class females and third-class males. Small family groups also had better outcomes than passengers traveling alone or in large families.

For any future predictive modeling, the dataset should be handled carefully: avoid target leakage, exclude non-informative identifiers, account for substantial missingness, and treat small subgroup estimates cautiously.

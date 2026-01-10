# kempner

[[_TOC_]]

## Description

The classical “no-9” Kempner series is
$1+1/2+\dots+1/8+1/10+\dots+1/18+1/20+\dots$ where the digit 9 is forbidden.
This and similar series converge, but *very slowly*, and the obtention of
their values with many (decimal, preferentially, or binary) digits is a
challenge.

One can represent exactly the Kempner series via alternating (or positive)
series having geometric convergence, making the computation of their values
with tens of thousands of digits amenable to personal computers.  This
involves coefficients related to the moments of certain measures.  See
[Moments in the exact summation of the curious series of Kempner type](https://doi.org/10.1080/00029890.2025.2554555)
(*The American Mathematical Monthly* **132**:10 (2025), 995-1006).  The last
preprint version is at [arXiv:2402.08525](https://arxiv.org/abs/2402.08525).

The present repository is initially to document implementations (back in
prehistoric times in 2012) of the formulas which were published in the above
reference.  The first installment of this repository contains only, besides
this short description, the two Maple files I attached in 2024 to the original
preprint version posted on [arXiv](https://arxiv.org).

> [!important]
> The two Maple files [kempner_base10_all.mpl](kempner_base10_all.mpl)
> and [kempner_2000digits.mpl](kempner_2000digits.mpl) are both almost
> identical up to translation into English with some earlier source I wrote
> in January 2012.
>
> The file [kempner_2000digits.mpl](kempner_2000digits.mpl)
> is now completely superseded by the SageMath code I wrote in February 2024
> to accompany my next manuscript
> [Measures for the summation of Irwin series](https://doi.org/10.5281/zenodo.18154150).
> See the
> sibling project [burnolmath/irwin](https://gitlab.com/burnolmath/irwin).
>
> As per [kempner_base10_all.mpl](kempner_base10_all.mpl), it handles
> only radix 10, but remains to this day the sole implementation of the
> formulas of my Kempner paper for more than one digit being excluded.
> I
> created this repository with the uncertain perspective to update it later
> with some new and more powerful numerical implementations.
>
> I do not document how to use the Maple files with extensions
> `.mpl` (but see comments therein) because I hold a Maple license
> only on some old hardware I am not using anymore, so I couldn't
> test now my own instructions.  This is also the reason why I do
> not attach the files with extension `.mw`.  However if you are
> familiar with Maple syntax, you will have not issue using the
> `.mpl` files.  Anyhow I am also attaching the outputs I obtained from
> them in February 2024.

## Bibliographical references

This repository is devoted to the formulas from:

- Moments in the exact summation of the curious series of Kempner type, *The
American Mathematical Monthly* **132**:10 (2025), 995-1006
([DOI](https://doi.org/10.1080/00029890.2025.2554555), preprint version at
[arXiv:2402.08525](https://arxiv.org/abs/2402.08525)).

The formulas are generalized to Irwin series in:

- Measures for the summation of Irwin series, *Integers* **26**:A11 (2026), 20pp
([DOI](https://doi.org/10.5281/zenodo.18154150)).

Refer to the sibling project
[burnolmath/irwin](https://gitlab.com/burnolmath/irwin) for details and
additional bibliographical references.

## License

The files in this repository are distributed under the
CC-BY-SA 4.0 License.  See [LICENSE](LiCENSE).

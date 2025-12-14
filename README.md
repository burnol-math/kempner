# kempner

[[_TOC_]]

## Description

A Kempner series is (originally) a sub-series of the harmonic series where the
kept denominators are not allowed to contain some digits in a given radix, for
example the digit `9` in radix `10`.  Such series converge, but *very slowly*,
and the obtention of their values with many (decimal, preferentially, or
binary) digits is a challenge.  The concept was extended by Irwin to requiring
specific digits to have each a given exact number of occurrences (rather than
only being excluded).  It can be further extended to excluding certain words
(i.e. multi-digit strings) or counting them, and doing this not only for one
word but also for more than one.  Various other types of extensions of the
concept exist.  Although the topic is more than one century old, the
theoretical research is only in its beginnings.

I first encountered the topic in late 2011 and worked on it a bit in early
January 2012.  I discovered then that one could represent exactly the Kempner
series via alternating (or positive) series with geometric convergence, where
the coefficients are related to moments of certains measures and these moments
can be computed by certain (linear, but full) recurrences.  Then in February
2024 I decided to revisit that old (somewhat elementary) material and to
prepare it for publication. It has now appeared (September 2025 for the online version)
as
[Moments in the exact summation of the curious series of Kempner type](https://doi.org/10.1080/00029890.2025.2554555)
(*The American Mathematical Monthly* **132**:10 (2025), 995-1006).  The last preprint version is at [arXiv:2402.08525](https://arxiv.org/abs/2402.08525).

This
repository is initially to document implementations of my January 2012
formulas as presented in the above manuscript in February 2024.  The first
installment of this repository contains only, besides this short description,
the two Maple files I joined with my manuscript of February 2024, together
with their outputs.  It is possible that in future the repository will get
extended with further implementations, or with further theory; some ideas of
January 2012 are not yet incorporated into any of my 2024 manuscripts.

> [!important]
> The two Maple files [kempner_base10_all.mpl](kempner_base10_all.mpl)
> and [kempner_2000digits.mpl](kempner_2000digits.mpl) are both almost
> identical up to translation into English with some earlier source I wrote
> in January 2012.
>
> The file [kempner_2000digits.mpl](kempner_2000digits.mpl)
> is now completely superseded by the SageMath code I wrote in February 2024
> to accompany my next manuscript
> [Measures for the summation of Irwin series](https://arxiv.org/abs/2402.09083).
> See the
> sibling project [burnolmath/irwin](https://gitlab.com/burnolmath/irwin).
>
> As per [kempner_base10_all.mpl](kempner_base10_all.mpl), it handles
> only radix 10, but remains to this day the sole implementation (apart
> from some Python prototype I wrote in February 2024 using only the
> `float` type precision and which handles arbitrary base) of my
> Kempner formulas for more than one digit being excluded.
> I will probably at some point re-implement in a more complete
> manner my formulas in either SageMath or perhaps directly using
> the MPFR library (the goal being to obtain many digits).  So I
> created this repository with the uncertain perspective to update it later
> with some new and more powerful numerical implementations.
>
> Whether this repository will also be used for archiving code handling
> words of length greater than 1 is yet undecided.
>
> I do not document how to use the Maple files with extensions
> `.mpl` (but see comments therein) because I hold a Maple license
> only on some old hardware I am not using anymore, so I couldn't
> test now my own instructions.  This is also the reason why I do
> not attach the files with extension `.mw`.  However if you are
> familiar with Maple syntax, you will have not issue using these
> files.  Anyhow I am also attaching the outputs I obtained from
> them in February 2024.

## Bibliographical references

This repository is devoted to the formulas first published in:

- Moments in the exact summation of the curious series of Kempner type, *The
American Mathematical Monthly* **132**:10 (2025), 995-1006
([DOI](https://doi.org/10.1080/00029890.2025.2554555), preprint version at
[arXiv:2402.08525](https://arxiv.org/abs/2402.08525)).

Having written this up for publication in February 2024 got me
started again on the topic and I obtained then a number of
additional results, always remaining at a somewhat elementary
level, because there never was any time to re-visit using more
powerful analytic machinery.

In particular, in

- Measures for the summation of Irwin series. Available at [arXiv:2402.09083](https://arxiv.org/abs/2402.09083),

I handled the more general Irwin series (associated with only one digit).
Refer to the sibling project
[burnolmath/irwin](https://gitlab.com/burnolmath/irwin) for details and
additional bibliographical references, inclusive of papers of mine, some of
which have already appeared in print attow.

## License

The files in this repository are distributed under the
CC-BY-SA 4.0 License.  See [LICENSE](LiCENSE).

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

I first encountered the topic in late 2011 and worked on it a bit in
January 2012.  Then in February 2024 I decided to revisit that old (somewhat
elementary) material and prepare it for publication.  This then induced me to
add various new results (always remaining at a somewhat elementary level,
because there never was any time to re-visit using more powerful analytic
machinery).

This repository is
initially to document implementations of the formulas from my February 2024
manuscript:

[Moments in the exact summation of the curious series of Kempner type](https://arxiv.org/abs/2402.08525)

This manuscript was accepted for publication by American Mathematical Monthly
in late 2024 and should appear there in late 2025 or early 2026.

The first installment of this repository will contain only besides this
short description the two Maple files I joined with my manuscript of February
2024, together with their outputs.

> [!important]
> The two Maple files [kempner_base10_all.mpl](kempner_base10_all.mpl)
> and [kempner_2000digits.mpl](kempner_2000digits.mpl) are both almost
> identical up to translation into English with some earlier source I wrote
> in January 2012.  [kempner_2000digits.mpl](kempner_2000digits.mpl) is
> completely superseded by the SageMath code I wrote in February 2024
> to accompany my other manuscript
> [Measures for the summation of Irwin series](https://arxiv.org/abs/2402.09083)
> and for which even more powerful versions are now available at the
> sibling project [burnolmath/irwin](https://gitlab.com/burnolmath/irwin).
>
> As per [kempner_base10_all.mpl](kempner_base10_all.mpl), it handles
> only radix 10, but remains to this day the sole implementation of my
> Kempner formulas for more than one digit being excluded.
> I will probably at some point re-implement in a more complete
> manner my formulas in either SageMath or perhaps directly using
> the MPFR library (the goal being to obtain many digits).  So I
> created this repository with the uncertain perspective to update it later
> with some new numerical implementation.
>
> Whether this repository will also be used for archiving code handling
> words of length greater than 1 is yet undecided.
>
> I am sorry I will not here document how to use the Maple files with
> extensions `.mpl` because I hold a Maple license only on some old
> hardware I am not using anymore, so I can't test.  This is also
> the reason why I do not attach the files with extension `.mw`.
> However if you are familiar with Maple syntax,
> you will have not issue using these files.  Anyhow I am also
> attaching the outputs I obtained from them...

## Bibliographical references

This repository is devoted to the formulas first published in:

- [Moments in the exact summation of the curious series of Kempner type](https://arxiv.org/abs/2402.08525) (to appear in American Mathematical Monthly, 2025 or 2026).

In a second installment
- [Measures for the summation of Irwin series](https://arxiv.org/abs/2402.09083)

I handled the Irwin variation, but only for one digit.  Refer to the sibling
project [burnolmath/irwin](https://gitlab.com/burnolmath/irwin) for details.

My two papers quoted above have not yet been published but some of my further
research has already appeared:

- Summing the "exactly one 42" and similar subsums of the harmonic series,  Advances in Applied Mathematics Volume 162, January 2025, 102791. [DOI](https://doi.org/10.1016/j.aam.2024.102791)
- Digamma function and general Fischer series in the theory of Kempner sums, Expositiones Mathematicae, Volume 42, Issue 6, December 2024, 125604. [DOI](https://doi.org/10.1016/j.exmath.2024.125604)
- Measures associated with certain ellipsephic harmonic series and the Allouche-Hu-Morin limit theorem, Acta Mathematica Hungarica (2025) [DOI](https://doi.org/10.1007/s10474-025-01525-3)

You will find at
[arXiv:burnol](https://arxiv.org/search/?searchtype=author&query=Burnol%2C+J)
some further manuscripts related to this topic, as well as earlier papers
doing fancy mathematics on some other topics.  Fancier mathematics of those times
is not yet public.

TODO: perhaps add some additional bibliographical references and do the
fancier earlier mathematics at long last.

## License

The files in this repository are distributed under the
CC-BY-SA 4.0 License.  See [LICENSE](LiCENSE).

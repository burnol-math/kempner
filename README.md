# kempner

[[_TOC_]]

## Kempner series

The classical “no-9” Kempner series is
$$\frac{1}{1} + \frac{1}{2} + \dots + \frac{1}{8} + \frac{1}{10} + \dots + \frac{1}{18} + \frac{1}{20} + \dots + \frac{1}{88} + \frac{1}{100} + \dots$$
where the digit 9 is forbidden.
This and similar series converge, but *very slowly*, and the obtention of
their values with many (decimal, preferentially, or binary) digits is a
challenge.

As shown in
[Moments in the exact summation of the curious series of Kempner type](https://doi.org/10.1080/00029890.2025.2554555)
(*The American Mathematical Monthly* **132**:10 (2025), 995-1006) and
[Measures for the summation of Irwin series](https://doi.org/10.5281/zenodo.18154150)
(*Integers* **26**:A11 (2026), 20pp.),  one can represent exactly the Kempner
series via alternating (or positive) series having geometric convergence,
making the computation of their values with tens of thousands of digits
amenable to personal computers.  This involves coefficients related to the
moments (or “complementary moments”, which perhaps I should have called
“co-moments”, for the positive series) of certain measures.

For mathematical details, see
https://burnolmath.gitlab.io/irwin/#the-new-series.

## This repository (May 2025)

The initial installment was only to make available two Maple files
from earlier times whose code comments I translated into English
in 2024 and attached to https://arxiv.org/abs/2402.08525 which was
the preprint of my AMM publication.

> [!important]
>
> The file [`kempner_2000digits.mpl`](kempner_2000digits.mpl)
> is now completely superseded by the SageMath code I wrote in February 2024
> and updated in May 2025 to accompany
> [Measures for the summation of Irwin series](https://doi.org/10.5281/zenodo.18154150).
> See the
> sibling project [burnolmath.gitlab.io/irwin](https://gitlab.com/burnolmath/irwin).
>
> I do not document how to use the Maple files with extensions
> `.mpl` (but see comments therein) because I hold a Maple license
> only on some old hardware I am not using anymore, so I couldn't
> test now my own instructions.  This is also the reason why I do
> not attach the files with extension `.mw`.  However if you are
> familiar with Maple syntax, you will have not issue using the
> `.mpl` files.  Anyhow I am also attaching the outputs I obtained from
> them.

## Update (April 2026)

I have now added a Python + [mpmath](https://mpmath.org) script
[`kempner.py`](kempner.py) which implements, for all bases, and all sets of
excluded digits, both the alternating series (via `kempner()`) of the AMM
article and its variant the positive series (`kempnerpos()`).

Running Python on file
[`test_kempner_base10_all.py`](test_kempner_base10_all.py) will confirm that
all 1021 Kempner series in base 10 are computed the same (each to 105
significant figures) by `kempner()` (alternating series) and `kempnerpos()`
(positive series).  Executing a `diff` as per the printed instructions to
`stdout` will confirm each value is computed with the same 100 decimal places
as were recorded in [`kempner_base10_all_out`](kempner_base10_all_out), which
was produced by the old Maple code.

We now give a few examples of use from within an Python interactive session.
Below are obtained 1000 decimal places for each of the Kempner series defined
by, respectively:

- base 11 and excluded digit 10,
- base 12 and excluded digits 10 and 11,
- base 13 and excluded digits 10, 11, and 12.

```text
$ python
<Python 3.13.3 banner>
>>> from kempner import *
>>> kempner(11, 10, 1002, silent=True, trunc=True)
'26.2833282048814207699401516874442229241887980925085989428035011768395362544352349985468191872038695638735650087945622219951263894381621767583428572371852651360535707924179928842414358481142842052760661977896375311810410779741484994666391421962014403347921206280925130566683425540634405088435097364385483768236904987003977589945566351501348764155055450187758956449563592684500155062624459232443706598487033841467847888257896764872952442003614614824058356225888841517771138353309244789738967007224973748228950052962884931811018647556641032169195514343360750243230214004048761399741616494871168620997427406093945521751458944285417093076589463521838942487490064485059210810155192346529701155583806329593173609473030289118116165049969500804763545620169979850354227584273054085669838938966992381721954490636669263559083162629188520604558331356094847499113874891303710852488227253148695856521780629140499987939589148008889098037777160057561478159137459691199650861275066295087429419157222311849695096233246051'
>>> kempner(12, [10, 11], 1002, silent=True, trunc=True)
'14.7339088292407616724550644277566276623901253772798618913881399467959951518286334708942665369993422051522691963496698148913623564621865970881623292095611885975376317728547004982871101472450507791041606626541057597092998144031574404105641964230680360173233594850096863815660975715944579128527367899155925764925795816611902070949899977649680967616860141305776927221891066081631090015710982425220508712353375252584993229610328393688081923290921945049276802803743398989821117980584292092144508526150345660229481373808783671845049485652772450597400020661841659584908439293158969933456918239540515628183326084285069302232278640360296365563715580521039425245781482268619506885921960808739221116587574882209960303767756300226434394934024892953769593797971859084168479605994010442568081134256073463090236662384697760374827174217885287073650914650472353693856533159860783701799891759652051524237073535160425403584383725989159571897983194078176047613841893948468452200843117585447242595255720243480059469741044185'
>>> kempner(13, [10, 11, 12], 1002, silent=True, trunc=True)
'10.8660131760769908514816459881899056536634355480478294388534954102640758671327926119140723855044318819574895019599351999089288468462777108769193194434232448306738720619633854203939918524604325699053578665642791875569503261282384111760492311589001727213526638304927962418170463326913198710744077334598502606323900032740581360339333985577802674078775491801206423634190779904144383736197533942569522003390136056743109258135156602444372705190844823300896420633437449976945271978643817420066731697647550726244371676007977832951374977827398232934822649777463733959475097594455986822068836605577446798040595643417851912271296884824450170876772039413529593885735418157741870249884257653941889407079105298055562308891846263069914106515555786235271594619481560957046564023688074464077177736201359523415680263633383804728374149241773470278474957171288970771182177099484831369480316996373346753324025797791404551485241807806627275533842534042016294197178275142397337157413605070160067478711736942143095907790522936'
```

Note that we pass the list of excluded digits as second argument to
`kempner()`, it is possible that in the AMM paper it is rather the set of
admissible digits which is used to index the Kempner sum.  Probably the Python
interface should rather be with some mutually exclusive keyword arguments
`admissible=...`, `excluded=...`.

One can also call the procedure directly from the command line:

```text
$ python kempner.py 10 9,8 52
ell is 3
basis is 10
List of excluded digits is [8, 9]
Last used: m = 25, cm = -1.217e-55
 not used: m = 26, cm = 8.836e-58
Last digits are 875749085(874)
K(10, [8, 9]) rounded to 52 significant figures is:
11.29158161683249138170633221349816010151212875749086
```

This interface maps only to `kempner()` and only handles the two mandatory
arguments (basis and comma separated excluded digits) and the first two
optional ones (number of significant figures and level).

> [!note]
>
> The second keyword parameter `ell` defaults to 3.  Set it to a higher
> value when using small bases 2, 3, 4 perhaps also 5.  But reduce it to 2
> for example when using base 16 or 20.
>
> The SageMath code at the
> sibling project [burnolmath/irwin](https://gitlab.com/burnolmath/irwin),
> which can handle Kempner series with one excluded digit, 
> proves to be in the case of base 10, excluded digit 9, and 1002
> significant figures, about 5x times faster than the Python code here.
>
> I have not tried to identify which optimizations in `irwin_v5.sage`
> explain this, but the code there has a much more complex organization
> in parts due to attempts at parallelization.  The Python code
> in [`kempner.py`](kempner.py) is much more straightforward and can
> get translated presumably very easily into the programming language
> of your choice.  It also has almost no memory impact.
> See comments therein.


## Bibliographical references

- Moments in the exact summation of the curious series of Kempner type, *The
American Mathematical Monthly* **132**:10 (2025), 995-1006
([DOI](https://doi.org/10.1080/00029890.2025.2554555)).

- Measures for the summation of Irwin series, *Integers* **26**:A11 (2026), 20pp
([DOI](https://doi.org/10.5281/zenodo.18154150)).

Refer to [burnolmath.gitlab.io/irwin](https://burnolmath.gitlab.io/irwin) for
mathematical details and additional bibliographical references.

## License

The files in this repository are distributed under the
CC-BY-SA 4.0 License.  See [LICENSE](LiCENSE).

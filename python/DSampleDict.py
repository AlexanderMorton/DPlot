from DProps import *
import ROOT

sampdict = {}

sampdict["TTBAR"] = DSampleProps("t#bart", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kRed, 0, 0), DFill(ROOT.kRed, 1001))

sampdict["WJETS"] = DSampleProps("W+jets", DLine(ROOT.kBlack, 1, 1),
        DMarker(92, 0, 0), DFill(92, 1001))

sampdict["ZJETS"] = DSampleProps("Z+jets", DLine(ROOT.kBlack, 1, 1),
        DMarker(95, 0, 0), DFill(95, 1001))

sampdict["DIBOSON"] = DSampleProps("Diboson", DLine(ROOT.kBlack, 1, 1),
        DMarker(5, 0, 0), DFill(5, 1001))

sampdict["SINGLETOP"] = DSampleProps("Single Top", DLine(ROOT.kBlack, 1, 1),
        DMarker(62, 0, 0), DFill(62, 1001))

sampdict["SIGNAL"] = DSampleProps("Signal", DLine(ROOT.kBlack, 1, 1),
        DMarker(619, 0, 0), DFill(619, 1001))

sampdict["QCD"] = DSampleProps("QCD", DLine(ROOT.kBlack, 1, 1),
        DMarker(619, 0, 0), DFill(619, 1001))

sampdict["DATA"] = DSampleProps("Data", DLine(ROOT.kBlack, 0, 0),
        DMarker(ROOT.kBlack, 20, 1), DFill(ROOT.kBlack, 0))


def getprocess(title):
    if "Period" in title or "period" in title:
        return "DATA"

    elif "ttbar" in title:
        return "TTBAR"

    elif "Wenu" in title or "Wmunu" in title or "Wtaunu" in title or \
            "Wbb" in title or "Wc" in title or "Wcc" in title:
        return "WJETS"

    elif "Zee" in title or "Zmumu" in title or "Ztautau" in title:
        return "ZJETS"

    elif "singletop" in title or "st_schan" in title or "st_Wtchan" in title:
        return "SINGLETOP"

    elif "WW" in title or "WZ" in title or "ZZ" in title:
        return "DIBOSON"

    elif "zprime" in title or "KKGluon" in title or "HVT" in title:
        return "SIGNAL"

    else:
        return "QCD"


def fix_style(samp, h):
    t, l, m, f = sampdict[getprocess(samp.title)]
    h.SetTitle(t)
    setline(h, l)
    setmarker(h, m)
    setfill(h, f)

    return h

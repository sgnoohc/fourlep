#!/bin/env python

import ROOT as r
import glob
import os
from os.path import exists


def getGenWeightSum(filename):
    f = r.TFile(filename)
    t = f.Get("Runs")
    genEventSumw = 0
    for i in t:
        genEventSumw += i.genEventSumw
    return genEventSumw

def getSMRewgtedGenWeightSum(filename):
    f = r.TFile(filename);
    Runs = f.Get("Runs");
    sumwgt = 0
    for ievent, event in enumerate(Runs):
        # print(ievent)
        if len(event.LHEReweightingSumw) != 0:
            # print("summing!")
            sumwgt += (event.genEventSumw * event.LHEReweightingSumw[0])
        # else:
            # print("skipping!")
        # print("------")
    return sumwgt

def parseYear(samplename):
    if "20UL18NanoAODv9" in samplename: return "2018"
    if "20UL17NanoAODv9" in samplename: return "2017"
    if "20UL16NanoAODv9" in samplename: return "2016"
    if "20UL16NanoAODAPVv9" in samplename: return "2016APV"

def parseLumi(samplename):
    if "20UL18NanoAODv9" in samplename: return 59.8
    if "20UL17NanoAODv9" in samplename: return 41.5
    if "20UL16NanoAODv9" in samplename: return 16.8
    if "20UL16NanoAODAPVv9" in samplename: return 19.5

if __name__ == "__main__":

    xsec_filename = "xsec.txt"
    xsecdb = dict([ [ x.split()[0][1:].replace("/","_")+"_v8", x.split()[1] ] for x in open(xsec_filename).readlines() ])

    WWZ_EFT = "/ceph/cms/store/user/phchang/VVVULSignalSamples/WWZ_RunIISummer20UL18NanoAODv9_FourleptonFilter_FilterFix_merged/WWZ-RunIISummer20UL18NanoAODv9_All_1M.root"
    genweight = getSMRewgtedGenWeightSum(WWZ_EFT)
    xsec = 0.1651 * 0.3272 * 0.3272 * 0.1009
    year = "Run2"
    lumi = 137.6
    print("{:300s},{:30.10f},{},{},{},{}".format(WWZ_EFT, xsec * 1000 * lumi / genweight, year, lumi, genweight, xsec))

    WZZ_EFT = "/ceph/cms/store/user/phchang/VVVULSignalSamples/WZZ_RunIISummer20UL18NanoAODv9_FourleptonFilter_FilterFix_merged/WZZ-RunIISummer20UL18NanoAODv9_All_1M.root"
    genweight = getSMRewgtedGenWeightSum(WZZ_EFT)
    xsec = 0.05565 * 0.10099 * 0.10099
    year = "Run2"
    lumi = 137.6
    print("{:300s},{:30.10f},{},{},{},{}".format(WZZ_EFT, xsec * 1000 * lumi / genweight, year, lumi, genweight, xsec))

    ZZZ_EFT = "/ceph/cms/store/user/phchang/VVVULSignalSamples/ZZZ_RunIISummer20UL18NanoAODv9_FourleptonFilter_FilterFix_merged/ZZZ4lepton_All.root"
    genweight = getSMRewgtedGenWeightSum(ZZZ_EFT)
    xsec = 0.01398 * 0.10099 * 0.10099 * 3
    year = "Run2"
    lumi = 137.6
    print("{:300s},{:30.10f},{},{},{},{}".format(ZZZ_EFT, xsec * 1000 * lumi / genweight, year, lumi, genweight, xsec))


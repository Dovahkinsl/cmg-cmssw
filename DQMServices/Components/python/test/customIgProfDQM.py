
import FWCore.ParameterSet.Config as cms

def customise(process):

#    process.dtDataIntegrityUnpacker.inputLabel = cms.untracked.InputTag('rawDataCollector')

#    process.DQMOfflineCosmics.remove(process.hcalOfflineDQMSource)

#    process.load("FWCore.Modules.printContent_cfi")
#    process.myPath1 = cms.Path( process.printContent )

    process.options = cms.untracked.PSet(
      wantSummary = cms.untracked.bool(True) 
    )

    process.DQMoutput.outputCommands.append('drop *')
    process.DQMoutput.outputCommands.append('keep *_MEtoEDMConverter_*_*')

#    process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#     ignoreTotal=cms.untracked.int32(1),
#     oncePerEventMode=cms.untracked.bool(False)
#    )

#Add the configuration for the Igprof running to dump profile snapshots:
    process.IgProfService = cms.Service("IgProfService",
             reportFirstEvent            = cms.untracked.int32(1),
             reportEventInterval         = cms.untracked.int32(25),
             reportToFileAtPostEvent     = cms.untracked.string("| gzip -c > IgProf.%I.gz")
             )

    process.load("DQMServices.Components.DQMStoreStats_cfi")
    process.stats = cms.Path(process.dqmStoreStats)
    process.schedule.insert(-2,process.stats)

    return(process)


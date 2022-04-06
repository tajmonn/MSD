#include "LORENCA_DOKONCZYC_capi_host.h"
static LORENCA_DOKONCZYC_host_DataMapInfo_T root;
static int initialized = 0;
__declspec( dllexport ) rtwCAPI_ModelMappingInfo *getRootMappingInfo()
{
    if (initialized == 0) {
        initialized = 1;
        LORENCA_DOKONCZYC_host_InitializeDataMapInfo(&(root), "LORENCA_DOKONCZYC");
    }
    return &root.mmi;
}

rtwCAPI_ModelMappingInfo *mexFunction() {return(getRootMappingInfo());}

#ifndef RTW_HEADER_LORENCA_DOKONCZYC_h_
#define RTW_HEADER_LORENCA_DOKONCZYC_h_
#include <stddef.h>
#include <string.h>
#include "rtw_modelmap_simtarget.h"
#ifndef LORENCA_DOKONCZYC_COMMON_INCLUDES_
#define LORENCA_DOKONCZYC_COMMON_INCLUDES_
#include <stdlib.h>
#include "sl_AsyncioQueue/AsyncioQueueCAPI.h"
#include "rtwtypes.h"
#include "sigstream_rtw.h"
#include "simtarget/slSimTgtSigstreamRTW.h"
#include "simtarget/slSimTgtSlioCoreRTW.h"
#include "simtarget/slSimTgtSlioClientsRTW.h"
#include "simtarget/slSimTgtSlioSdiRTW.h"
#include "simstruc.h"
#include "fixedpoint.h"
#include "raccel.h"
#include "slsv_diagnostic_codegen_c_api.h"
#include "rt_logging_simtarget.h"
#include "dt_info.h"
#include "ext_work.h"
#endif
#include "LORENCA_DOKONCZYC_types.h"
#include "multiword_types.h"
#include "rt_defines.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#define MODEL_NAME LORENCA_DOKONCZYC
#define NSAMPLE_TIMES (3) 
#define NINPUTS (0)       
#define NOUTPUTS (0)     
#define NBLOCKIO (6) 
#define NUM_ZC_EVENTS (0) 
#ifndef NCSTATES
#define NCSTATES (3)   
#elif NCSTATES != 3
#error Invalid specification of NCSTATES defined in compiler command
#endif
#ifndef rtmGetDataMapInfo
#define rtmGetDataMapInfo(rtm) (*rt_dataMapInfoPtr)
#endif
#ifndef rtmSetDataMapInfo
#define rtmSetDataMapInfo(rtm, val) (rt_dataMapInfoPtr = &val)
#endif
#ifndef IN_RACCEL_MAIN
#endif
typedef struct { real_T fc10ryf0wg ; real_T dyxwhs3ldi ; real_T mvt54jszau ;
real_T oldneziywo ; real_T altl2c2dou ; real_T iibsul51x1 ; } B ; typedef
struct { struct { void * AQHandles ; } fxoxjzkfy4 ; struct { void * AQHandles
; } ovuiamaqua ; struct { void * AQHandles ; } fzxj2uvlvj ; struct { void *
AQHandles ; } lgkkd140zh ; struct { void * AQHandles ; } btw0yhtfw0 ; struct
{ void * AQHandles ; } anb2izryaw ; struct { void * LoggedData ; } bwpleeu1ul
; } DW ; typedef struct { real_T ee3xhreh3c ; real_T iw3lslepvf ; real_T
clfoa0vq3n ; } X ; typedef struct { real_T ee3xhreh3c ; real_T iw3lslepvf ;
real_T clfoa0vq3n ; } XDot ; typedef struct { boolean_T ee3xhreh3c ;
boolean_T iw3lslepvf ; boolean_T clfoa0vq3n ; } XDis ; typedef struct {
rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ; struct P_ { real_T dydt_IC ;
real_T dxdt_IC ; real_T dzdt_IC ; real_T a_Value ; real_T b_Value ; real_T
c_Value ; } ; extern const char * RT_MEMORY_ALLOCATION_ERROR ; extern B rtB ;
extern X rtX ; extern DW rtDW ; extern P rtP ; extern mxArray *
mr_LORENCA_DOKONCZYC_GetDWork ( ) ; extern void mr_LORENCA_DOKONCZYC_SetDWork
( const mxArray * ssDW ) ; extern mxArray *
mr_LORENCA_DOKONCZYC_GetSimStateDisallowedBlocks ( ) ; extern const
rtwCAPI_ModelMappingStaticInfo * LORENCA_DOKONCZYC_GetCAPIStaticMap ( void )
; extern SimStruct * const rtS ; extern const int_T gblNumToFiles ; extern
const int_T gblNumFrFiles ; extern const int_T gblNumFrWksBlocks ; extern
rtInportTUtable * gblInportTUtables ; extern const char * gblInportFileName ;
extern const int_T gblNumRootInportBlks ; extern const int_T
gblNumModelInputs ; extern const int_T gblInportDataTypeIdx [ ] ; extern
const int_T gblInportDims [ ] ; extern const int_T gblInportComplex [ ] ;
extern const int_T gblInportInterpoFlag [ ] ; extern const int_T
gblInportContinuous [ ] ; extern const int_T gblParameterTuningTid ; extern
DataMapInfo * rt_dataMapInfoPtr ; extern rtwCAPI_ModelMappingInfo *
rt_modelMapInfoPtr ; void MdlOutputs ( int_T tid ) ; void
MdlOutputsParameterSampleTime ( int_T tid ) ; void MdlUpdate ( int_T tid ) ;
void MdlTerminate ( void ) ; void MdlInitializeSizes ( void ) ; void
MdlInitializeSampleTimes ( void ) ; SimStruct * raccel_register_model (
ssExecutionInfo * executionInfo ) ;
#endif

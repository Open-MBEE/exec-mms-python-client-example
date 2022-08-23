# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**name** | **str** |  | 
**id** | **str** |  | [optional] 
**schema** | **str** | Acceptable values depends on the specific build and implementation (ex. default, cameo, jupyter), if a value isn&#39;t supported, will fall back to default. This can influence the project&#39;s underlying schema used and additional validation or processing when getting or updating elements. | [optional]  if omitted the server will use the default value of "default"
**project_id** | **str** |  | [optional] [readonly] 
**creator** | **str** |  | [optional] [readonly] 
**doc_id** | **str** |  | [optional] [readonly] 
**created** | **str** |  | [optional] [readonly] 
**modifier** | **str** |  | [optional] [readonly] 
**modified** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



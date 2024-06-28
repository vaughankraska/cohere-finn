from enum import StrEnum

from community.tools import (
    ArxivRetriever,
    Category,
    ClinicalTrials,
    LlamaIndexUploadPDFRetriever,
    ManagedTool,
    PubMedRetriever,
    WolframAlpha,
)


class CommunityToolName(StrEnum):
    Arxiv = "arxiv"
    Pub_Med = "pub_med"
    File_Upload_LlamaIndex = "file_reader_llamaindex"
    Wolfram_Alpha = "wolfram_alpha"
    ClinicalTrials = "clinical_trials"


COMMUNITY_TOOLS = {
    CommunityToolName.Arxiv: ManagedTool(
        name=CommunityToolName.Arxiv,
        display_name="Arxiv",
        implementation=ArxivRetriever,
        parameter_definitions={
            "query": {
                "description": "Query for retrieval.",
                "type": "str",
                "required": True,
            }
        },
        is_visible=True,
        is_available=ArxivRetriever.is_available(),
        error_message="ArxivRetriever is not available.",
        category=Category.DataLoader,
        description="Retrieves documents from Arxiv.",
    ),
    CommunityToolName.Pub_Med: ManagedTool(
        name=CommunityToolName.Pub_Med,
        display_name="PubMed",
        implementation=PubMedRetriever,
        parameter_definitions={
            "query": {
                "description": "Query for retrieval.",
                "type": "str",
                "required": True,
            }
        },
        is_visible=True,
        is_available=PubMedRetriever.is_available(),
        error_message="PubMedRetriever is not available.",
        category=Category.DataLoader,
        description="Retrieves documents from Pub Med.",
    ),
    CommunityToolName.File_Upload_LlamaIndex: ManagedTool(
        name=CommunityToolName.File_Upload_LlamaIndex,
        display_name="File Reader",
        implementation=LlamaIndexUploadPDFRetriever,
        is_visible=True,
        is_available=LlamaIndexUploadPDFRetriever.is_available(),
        error_message="LlamaIndexUploadPDFRetriever is not available.",
        category=Category.FileLoader,
        description="Retrieves documents from a file using LlamaIndex.",
    ),
    CommunityToolName.Wolfram_Alpha: ManagedTool(
        name=CommunityToolName.Wolfram_Alpha,
        display_name="Wolfram Alpha",
        implementation=WolframAlpha,
        is_visible=False,
        is_available=WolframAlpha.is_available(),
        error_message="WolframAlphaFunctionTool is not available, please set the WOLFRAM_APP_ID environment variable.",
        category=Category.Function,
        description="Evaluate arithmetic expressions.",
    ),
    CommunityToolName.ClinicalTrials: ManagedTool(
        name=CommunityToolName.ClinicalTrials,
        display_name="Clinical Trials",
        implementation=ClinicalTrials,
        is_visible=True,
        is_available=ClinicalTrials.is_available(),
        error_message="ClinicalTrialsTool is not available.",
        category=Category.Function,
        description="Retrieves clinical studies from ClinicalTrials.gov.",
        parameter_definitions={
            "condition": {
                "description": "Filters clinical studies to a specified disease or condition",
                "type": "str",
                "required": False,
            },
            "location": {
                "description": "Filters clinical studies to a specified city, state, or country.",
                "type": "str",
                "required": False,
            },
            "intervention": {
                "description": "Filters clinical studies to a specified drug or treatment.",
                "type": "str",
                "required": False,
            },
            "is_recruiting": {
                "description": "Filters clinical studies to those that are actively recruiting.",
                "type": "bool",
                "required": False,
            },
        },
    ),
}

# For main.py cli setup script
COMMUNITY_TOOLS_SETUP = {
    CommunityToolName.Wolfram_Alpha: {
        "secrets": {
            "WOLFRAM_ALPHA_APP_ID": None,  # default value
        },
    },
}

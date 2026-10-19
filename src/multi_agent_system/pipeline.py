from .agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:
    state = {}

    #search agent working
    print("\n" + "="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent = build_search_agent()
    serach_result = search_agent.invoke({
        "messages" : [("user", f"find recent, reliable and detailed information about: {topic}")]
    })
    state["search_result"] = serach_result["messages"][-1].content

    print("\n search result ", state["search_result"])



# step 2



#search agent working
    print("\n" + "="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)

    reader_agent = reader_agent()
    reader_agent.invoke({
        "messages": [("user", 
                      f"Based on the following search results about '{topic}',"
                      f"pick the most relevant URL and  scrape it for deeper content.\n\n"
                      f"Search Results: \n{state['search_result'][:800]}")]
    })
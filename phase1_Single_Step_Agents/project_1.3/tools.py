from file_reader import read_text_file
from transaction_parser import filter_transaction, sum_amounts

class AgentTools:

    def read_statement(self):

        print("\n[Tool Execution]: read_statement\n")
        
        # def read_text_file(file_path: str):

        #     try:
        #         with open(file_path, "r") as f:
        #             content = f.read()
                
        #         return{
        #             "success": True,
        #             "content": content
        #         }
            
        #     except Exception as e:

        #         return{
        #             "succuess": False,
        #             "error": str(e)
        #         } 
        
        return read_text_file("phase1/project_1.3/data/bofa_statement.txt")
    
    def filter_and_sum(self, content: str, keyword: str) -> dict:

        """
        Extract transactions by keyword, then sum them
        """

        print(f"\n[Tool Execution]: filter_and_sum('{keyword}')\n")

        # 1. filter transactions
        transactions = filter_transaction(content, keyword)

        if not transactions:
            return {
                "found":False,
                "count": 0,
                "total": 0,
                "message": f"No transactions found with {keyword}"
            }
        
        total_transactions = sum_amounts(transactions)

        return {
            "found": True,
            "count": len(transactions),
            "total": total_transactions,
            "transactions": transactions[:5],  # First 5 as preview
            "message": f"Found {len(transactions)} transactions totaling ${abs(total_transactions):.2f}"
        }

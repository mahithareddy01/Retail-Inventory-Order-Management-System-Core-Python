from typing import Optional, List, Dict
from src.config import get_supabase

class OrderDao:
    def __init__(self):
        self._sb = get_supabase()

    # Create order and return the inserted row
    def create_order(self, customer_id: int, total_amount: float = 0.0, status: str = "PLACED") -> Optional[Dict]:
        payload = {"customer_id": customer_id, "total_amount": total_amount, "status": status}
        self._sb.table("orders").insert(payload).execute()
        # Fetch latest order for this customer
        resp = self._sb.table("orders")\
            .select("*")\
            .eq("customer_id", customer_id)\
            .order("order_id", desc=True)\
            .limit(1)\
            .execute()
        return resp.data[0] if resp.data else None

   
    def create_order_items(self, items: list) -> None:
   
        self._sb.table("order_items").insert(items).execute()

    # Fetch order by ID
    def get_order_by_id(self, order_id: int) -> Optional[Dict]:
        resp = self._sb.table("orders").select("*").eq("order_id", order_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    # Fetch order items
    def get_order_items(self, order_id: int) -> List[Dict]:
        resp = self._sb.table("order_items").select("*").eq("order_id", order_id).execute()
        return resp.data or []

    # List orders by customer
    def list_orders_by_customer(self, customer_id: int) -> List[Dict]:
        resp = self._sb.table("orders").select("*").eq("customer_id", customer_id).execute()
        return resp.data or []

    # Update order status
    def update_order_status(self, order_id: int, status: str) -> Optional[Dict]:
        self._sb.table("orders").update({"status": status}).eq("order_id", order_id).execute()
        return self.get_order_by_id(order_id)
    # List all orders
    def list_orders(self) -> list:
        resp = self._sb.table("orders").select("*").execute()
        return resp.data or []
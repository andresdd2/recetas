import { Outlet } from "react-router-dom";
import Navbar from "@/components/Navbar";

export default function DashboardLayout() {
  return (
    <div>
      <Navbar />
      <main className="max-w-5xl mx-auto px-4 py-8">
        <Outlet />
      </main>
    </div>
  );
}

# /* Global Background Image for Entire App */
# [data-testid="stAppViewContainer"], 
# [data-testid="stSidebar"], 
# [data-testid="stHeader"], 
# [data-testid="stFooter"] {
#     background: url('https://img.freepik.com/free-vector/clean-medical-background-vector_53876-175203.jpg?ga=GA1.1.968891202.1731431691&semt=ais_hybrid') no-repeat center center fixed !important;
#     background-size: cover !important;
# }

# /* Sidebar Customization */
# [data-testid="stSidebar"] {
#     background: rgba(0, 0, 0, 0.9) !important;
#     color: #FAD7A0 !important;
#     box-shadow: 4px 0px 10px rgba(255, 255, 255, 0.3);
#     padding: 20px;
#     border-radius: 0 15px 15px 0;
# }

# /* Header Text Styling */
# h1, h2, h3 {
#     color: black !important;
# }

# h1 {
#     font-size: 45px !important;
#     text-align: center;
#     font-weight: bold;
#     text-shadow: 3px 3px 10px rgba(255, 255, 255, 0.6);
#     animation: fadeIn 1.2s ease-in-out;
# }

# h2 {
#     font-size: 32px;
#     font-weight: bold;
#     text-shadow: 2px 2px 6px rgba(255, 255, 255, 0.5);
#     animation: slideIn 1.2s ease-in-out;
# }

# h3 {
#     font-size: 24px;
#     font-weight: bold;
# }

# /* Paragraph & List Styling */
# p, ul {
#     font-size: 18px;
#     color: #154360;
#     font-weight: normal;
#     background: rgba(255, 255, 255, 0.7);
#     padding: 15px;
#     border-radius: 12px;
#     box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.2);
#     transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
# }

# p:hover, ul:hover {
#     transform: scale(1.03);
#     box-shadow: 5px 5px 18px rgba(0, 0, 0, 0.3);
# }

# /* Buttons */
# .stButton>button {
#     background: linear-gradient(135deg, #2874A6, #1A5276) !important;
#     color: white !important;
#     font-size: 16px;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 12px 20px;
#     border: none;
#     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
#     transition: all 0.3s ease-in-out;
# }

# .stButton>button:hover {
#     background: linear-gradient(135deg, #154360, #1A5276) !important;
#     transform: translateY(-3px);
#     box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.5);
# }

# /* Input Box */
# .stTextInput>div>div>input {
#     background: rgba(200, 200, 255, 0.8) !important;
#     color: #154360 !important;
#     font-size: 16px;
#     padding: 10px;
#     border-radius: 8px;
#     border: 1px solid #2E86C1 !important;
#     transition: all 0.3s ease-in-out;
# }

# .stTextInput>div>div>input:focus {
#     background: rgba(255, 255, 255, 0.9) !important;
#     border: 1px solid #154360 !important;
# }

# /* Animations */
# @keyframes fadeIn {
#     0% { opacity: 0; transform: translateY(-15px); }
#     100% { opacity: 1; transform: translateY(0); }
# }

# @keyframes slideIn {
#     0% { opacity: 0; transform: translateX(-30px); }
#     100% { opacity: 1; transform: translateX(0); }
# }

# @keyframes pulse {
#     0% { transform: scale(1); }
#     50% { transform: scale(1.04); }
#     100% { transform: scale(1); }
# }

# /* Animated Elements */
# .animated-text {
#     animation: fadeIn 1.5s ease-in-out, pulse 3s infinite alternate;
# }

# /* Cards */
# .stCard {
#     background: rgba(255, 255, 255, 0.8);
#     padding: 15px;
#     border-radius: 15px;
#     box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
#     transition: all 0.3s ease-in-out;
# }

# .stCard:hover {
#     transform: translateY(-5px);
#     box-shadow: 6px 6px 18px rgba(0, 0, 0, 0.3);
# }

# /* Upload Sections Container - Flexbox */
# .report-section {
#     display: flex;
#     justify-content: center;
#     gap: 20px;
#     flex-wrap: wrap;
#     padding: 10px;
# }

# /* Upload Sections - Card Style */
# .report-container {
#     background: rgba(255, 255, 255, 0.9);
#     padding: 20px;
#     border-radius: 12px;
#     box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.2);
#     text-align: center;
#     transition: all 0.3s ease-in-out;
#     width: 30%;
#     min-width: 280px;
#     margin-bottom: 20px;
# }

# /* Upload Buttons */
# .upload-button {
#     background: linear-gradient(135deg, #2874A6, #1A5276) !important;
#     color: white !important;
#     font-size: 14px;
#     font-weight: bold;
#     padding: 10px;
#     border-radius: 8px;
#     width: 100%;
#     text-align: center;
#     box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
#     transition: all 0.3s ease-in-out;
#     margin-top: 20px;
# }

# /* Query Container */
# .query-container {
#     background: rgba(255, 255, 255, 0.9);
#     padding: 20px;
#     border-radius: 10px;
#     box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
#     margin-top: 20px;
# }

# /* Query Button */
# .query-button {
#     background: linear-gradient(135deg, #2874A6, #1A5276) !important;
#     color: blue !important;
#     font-size: 16px;
#     font-weight: bold;
#     padding: 25px;
#     border-radius: 10px;
#     text-align: center;
#     box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
#     transition: all 0.3s ease-in-out;
# }

# /* Alert Styles */
# .alert {
#     background-color: #d4edda;
#     color: #155724;
#     padding: 15px;
#     margin-top: 20px;
#     border-radius: 5px;
#     border: 1px solid #c3e6cb;
# }

# /* Hover Effects */
# .hover-shadow {
#     display: inline-block;
#     transition: all 0.3s ease;
# }

# .hover-shadow:hover {
#     text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);
#     color: #1abc9c;
# }

# /* Media Query for Mobile Devices */
# @media (max-width: 768px) {
#     h1 {
#         text-align: center !important;
#         font-size: 22px !important;
#     }
#     h2 {
#         font-size: 24px !important;
#     }

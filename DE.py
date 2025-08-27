<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Infographic: Hành Trình Chuyển Đổi Số của PFS LTD</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Brilliant Blues -->
    <!-- Application Structure Plan: The infographic follows a narrative structure, guiding the user from PFS LTD's current state to its future vision. It starts with a high-level overview (Current State, Challenges, Opportunities), then delves into the core strategy (The 3-Year Roadmap). This is followed by measurable outcomes (KPIs) and the supporting network (Ecosystem). The story is grounded in proven principles (Lessons from FPT/Kodak). This top-down, narrative flow was chosen to make a complex business strategy digestible and compelling for stakeholders. -->
    <!-- Visualization & Content Choices:
    - Current State: Report Info -> SWOT-like analysis -> Goal: Inform -> Viz: Styled HTML Cards -> Justification: Provides a quick, qualitative summary without chart clutter. Method: HTML/CSS.
    - 3-Year Roadmap: Report Info -> Phased plan -> Goal: Organize/Change -> Viz: HTML/CSS Timeline -> Justification: Clearly shows progression over time without complex libraries, adhering to NO SVG/Mermaid rule. Method: HTML/CSS.
    - KPIs: Report Info -> Percentage-based targets -> Goal: Compare -> Viz: Bar Chart -> Justification: Ideal for comparing quantitative goals across different categories and years. Method: Chart.js (Canvas).
    - Ecosystem: Report Info -> Company relationships -> Goal: Organize/Relationships -> Viz: HTML/CSS Diagram -> Justification: Simple, clear visualization of key partnerships. Method: HTML/CSS.
    - FPT vs Kodak: Report Info -> Comparative performance -> Goal: Compare -> Viz: Grouped Bar Chart -> Justification: Directly contrasts the financial outcomes of the two strategic approaches. Method: Chart.js (Canvas). -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8F9FA;
            color: #343A40;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 400px;
            }
        }
        .timeline-item {
            position: relative;
            padding-bottom: 2rem;
            padding-left: 2.5rem;
        }
        .timeline-item:not(:last-child) {
            border-left: 2px solid #007BFF;
        }
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -0.7rem;
            top: 0;
            width: 1.25rem;
            height: 1.25rem;
            border-radius: 50%;
            background-color: #007BFF;
            border: 4px solid #F8F9FA;
        }
    </style>
</head>
<body class="antialiased">

    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">

        <header class="text-center mb-16">
            <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 leading-tight">
                <span class="block">Hành Trình Chuyển Đổi Số Của</span>
                <span class="block text-blue-600 mt-2">PFS LTD</span>
            </h1>
            <p class="mt-4 text-lg text-gray-600 max-w-3xl mx-auto">Từ xưởng may truyền thống tại Hóc Môn đến doanh nghiệp dệt may 4.0, sẵn sàng dẫn đầu trong kỷ nguyên số.</p>
        </header>

        <section id="current-state" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Điểm Xuất Phát: Một Doanh Nghiệp SME Đầy Tiềm Năng</h2>
            <p class="text-center text-gray-600 max-w-2xl mx-auto mb-12">PFS LTD, một doanh nghiệp sản xuất dệt may tại Hóc Môn, đang đứng trước một bước ngoặt chiến lược. Dưới đây là bối cảnh hiện tại, những thách thức và cơ hội vàng đang chờ đợi.</p>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="bg-white rounded-lg shadow-md p-6 border-l-4 border-blue-500">
                    <h3 class="text-xl font-bold mb-3 text-gray-800">Hiện Trạng</h3>
                    <p class="text-gray-600">Sở hữu xưởng sản xuất, có năng lực kiểm soát chất lượng trực tiếp và ban lãnh đạo đã có nhận thức ban đầu về tầm quan trọng của hiện diện số.</p>
                </div>
                <div class="bg-white rounded-lg shadow-md p-6 border-l-4 border-yellow-500">
                    <h3 class="text-xl font-bold mb-3 text-gray-800">Thách Thức</h3>
                    <p class="text-gray-600">Vận hành thủ công dẫn đến hiệu quả thấp, cạnh tranh gay gắt về giá và khả năng tiếp cận thị trường còn hạn chế.</p>
                </div>
                <div class="bg-white rounded-lg shadow-md p-6 border-l-4 border-green-500">
                    <h3 class="text-xl font-bold mb-3 text-gray-800">Cơ Hội</h3>
                    <p class="text-gray-600">Tận dụng chính sách hỗ trợ chuyển đổi số của địa phương và đáp ứng nhu cầu ngày càng cao của thị trường B2B về sự minh bạch và tốc độ.</p>
                </div>
            </div>
        </section>

        <section id="roadmap" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Lộ Trình Chuyển Đổi 3 Năm</h2>
            <p class="text-center text-gray-600 max-w-2xl mx-auto mb-12">Một kế hoạch chi tiết theo từng giai đoạn, tập trung vào việc xây dựng một "bánh đà" tăng trưởng bền vững, biến thách thức thành lợi thế cạnh tranh.</p>
            <div>
                <div class="timeline-item">
                    <h3 class="text-2xl font-bold text-blue-600">Năm 1: Nền Tảng Vững Chắc</h3>
                    <p class="font-semibold text-gray-700 mt-1 mb-3">Tối ưu hóa nội bộ, xây dựng "xương sống số" và tạo ra nền tảng dữ liệu sạch.</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Triển khai hệ thống ERP tinh gọn để quản lý kho, sản xuất, bán hàng.</li>
                        <li>Số hóa 100% giao dịch bằng hóa đơn điện tử và chữ ký số.</li>
                        <li>Định hình tầm nhìn mới: "Nhà cung cấp Dệt may Thông minh và Linh hoạt".</li>
                    </ul>
                </div>
                <div class="timeline-item">
                    <h3 class="text-2xl font-bold text-blue-600">Năm 2: Lấy Khách Hàng B2B Làm Trung Tâm</h3>
                    <p class="font-semibold text-gray-700 mt-1 mb-3">Biến công nghệ thành lợi thế bán hàng và tạo ra trải nghiệm vượt trội cho đối tác.</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Xây dựng Cổng thông tin Đối tác B2B cho phép đặt hàng và theo dõi online.</li>
                        <li>Đào tạo đội ngũ kinh doanh sử dụng dữ liệu để tư vấn hiệu quả hơn.</li>
                        <li>Thử nghiệm dịch vụ mới: "Thiết kế và Sản xuất Mẫu theo yêu cầu".</li>
                    </ul>
                </div>
                <div class="timeline-item">
                    <h3 class="text-2xl font-bold text-blue-600">Năm 3: Đột Phá Mô Hình Kinh Doanh</h3>
                    <p class="font-semibold text-gray-700 mt-1 mb-3">Sử dụng dữ liệu để ra quyết định thông minh và tạo ra các dòng doanh thu mới.</p>
                    <ul class="list-disc list-inside text-gray-600 space-y-1">
                        <li>Phân tích dữ liệu bán hàng để dự báo xu hướng và tối ưu hóa sản xuất.</li>
                        <li>Khởi động chương trình "Sáng kiến Cải tiến Xưởng" để thúc đẩy văn hóa đổi mới.</li>
                        <li>Ra mắt thương hiệu con về nguyên phụ liệu "xanh", bền vững.</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="kpis" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Đo Lường Thành Công: Các Chỉ Số Mục Tiêu</h2>
            <p class="text-center text-gray-600 max-w-2xl mx-auto mb-12">Chuyển đổi số phải được đo lường bằng những kết quả cụ thể. Dưới đây là các chỉ số hiệu suất chính (KPI) mà PFS LTD kỳ vọng đạt được qua từng giai đoạn.</p>
            <div class="bg-white rounded-lg shadow-md p-6">
                <div class="chart-container">
                    <canvas id="kpiChart"></canvas>
                </div>
            </div>
        </section>

        <section id="ecosystem" class="mb-20">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Hệ Sinh Thái Hỗ Trợ: Sức Mạnh Cộng Hưởng</h2>
            <p class="text-center text-gray-600 max-w-2xl mx-auto mb-12">PFS LTD không đơn độc trên hành trình này. Một hệ sinh thái gồm các đối tác về tri thức, công nghệ và chuỗi cung ứng sẽ là bệ phóng cho sự phát triển.</p>
            <div class="grid md:grid-cols-5 gap-4 items-center text-center">
                <div class="bg-white rounded-lg shadow-md p-4 h-full flex flex-col justify-center">
                    <h4 class="font-bold text-teal-600">UTH TPHCM</h4>
                    <p class="text-sm text-gray-500">Đối Tác Tri Thức</p>
                    <p class="text-xs mt-2">Cung cấp nhân lực CNTT, R&D về logistics & chuỗi cung ứng.</p>
                </div>
                <div class="text-2xl text-gray-400 font-light">➔</div>
                <div class="bg-white rounded-lg shadow-md p-6 border-4 border-blue-500 md:col-span-1">
                    <h4 class="font-bold text-blue-600 text-lg">PFS LTD</h4>
                    <p class="text-sm text-gray-500">Doanh Nghiệp Cốt Lõi</p>
                </div>
                <div class="text-2xl text-gray-400 font-light">➔</div>
                <div class="bg-white rounded-lg shadow-md p-4 h-full flex flex-col justify-center">
                    <h4 class="font-bold text-purple-600">Đối Tác Cung Ứng</h4>
                    <p class="text-sm text-gray-500">(VD: Sang Kỳ)</p>
                    <p class="text-xs mt-2">Cung cấp máy móc, thiết bị chuyên ngành dệt may tại địa phương.</p>
                </div>
            </div>
        </section>

        <section id="lessons" class="mb-12">
            <h2 class="text-3xl font-bold text-center text-gray-800 mb-12">Bài Học Kinh Nghiệm: FPT và Kodak</h2>
            <p class="text-center text-gray-600 max-w-2xl mx-auto mb-12">Lộ trình của PFS LTD được xây dựng dựa trên những bài học sâu sắc từ sự thành công của FPT trong việc kiến tạo tương lai số và thất bại của Kodak khi không dám thay đổi.</p>
            <div class="bg-white rounded-lg shadow-md p-6">
                 <div class="chart-container">
                    <canvas id="fptKodakChart"></canvas>
                </div>
            </div>
             <div class="grid md:grid-cols-2 gap-8 mt-8">
                <div class="bg-green-50 border-l-4 border-green-500 p-4 rounded-r-lg">
                    <h4 class="font-bold text-green-800">Bài học từ FPT</h4>
                    <p class="text-green-700 mt-2">Can đảm tự đột phá, xây dựng hệ sinh thái sản phẩm "Made by FPT" và đầu tư mạnh mẽ vào văn hóa đổi mới sáng tạo.</p>
                </div>
                <div class="bg-red-50 border-l-4 border-red-500 p-4 rounded-r-lg">
                    <h4 class="font-bold text-red-800">Bài học từ Kodak</h4>
                    <p class="text-red-700 mt-2">Tê liệt chiến lược vì sợ "tự hủy hoại" mảng kinh doanh cốt lõi, và thất bại trong việc xây dựng mô hình kinh doanh mới.</p>
                </div>
            </div>
        </section>

    </div>

    <footer class="bg-gray-800 text-white mt-12">
        <div class="max-w-6xl mx-auto py-6 px-4 sm:px-6 lg:px-8 text-center text-sm">
            <p>Infographic được tạo ra để phân tích và trực quan hóa chiến lược chuyển đổi số cho PFS LTD.</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {

            const processLabel = (label) => {
                if (typeof label !== 'string' || label.length <= 16) {
                    return label;
                }
                const words = label.split(' ');
                const lines = [];
                let currentLine = '';
                for (const word of words) {
                    if ((currentLine + ' ' + word).trim().length > 16) {
                        lines.push(currentLine.trim());
                        currentLine = word;
                    } else {
                        currentLine = (currentLine + ' ' + word).trim();
                    }
                }
                if (currentLine) {
                    lines.push(currentLine.trim());
                }
                return lines;
            };

            const tooltipTitleCallback = (tooltipItems) => {
                const item = tooltipItems[0];
                let label = item.chart.data.labels[item.dataIndex];
                if (Array.isArray(label)) {
                    return label.join(' ');
                }
                return label;
            };

            const kpiCtx = document.getElementById('kpiChart').getContext('2d');
            const kpiLabels = [
                'Giảm sai sót vận hành', 
                'Tăng tỷ lệ khách hàng quay lại', 
                'Giảm thời gian xử lý đơn hàng', 
                'Tối ưu hóa lượng hàng tồn kho', 
                'Tăng năng suất xưởng'
            ];
            new Chart(kpiCtx, {
                type: 'bar',
                data: {
                    labels: kpiLabels.map(processLabel),
                    datasets: [
                        {
                            label: 'Năm 1',
                            data: [30, 0, 0, 0, 0],
                            backgroundColor: '#007BFF',
                        },
                        {
                            label: 'Năm 2',
                            data: [0, 20, 50, 0, 0],
                            backgroundColor: '#00C49F',
                        },
                        {
                            label: 'Năm 3',
                            data: [0, 0, 0, 25, 10],
                            backgroundColor: '#FFC107',
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Các Chỉ Số Mục Tiêu Qua Từng Năm (%)',
                            font: { size: 18, weight: 'bold' },
                            padding: { top: 10, bottom: 20 }
                        },
                        tooltip: {
                            callbacks: {
                                title: tooltipTitleCallback,
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    if (context.parsed.y !== null) {
                                        label += context.parsed.y + '%';
                                    }
                                    return label;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Tỷ lệ Cải thiện (%)'
                            }
                        },
                        x: {
                            ticks: {
                                autoSkip: false,
                                maxRotation: 0,
                                minRotation: 0
                            }
                        }
                    }
                }
            });

            const fptKodakCtx = document.getElementById('fptKodakChart').getContext('2d');
            new Chart(fptKodakCtx, {
                type: 'bar',
                data: {
                    labels: ['Doanh Thu (tỷ USD)', ['Thị Phần', '(%)']],
                    datasets: [{
                        label: 'FPT (Sau CĐS)',
                        data: [2.2, 61],
                        backgroundColor: '#00C49F',
                    }, {
                        label: 'Kodak (Thời đỉnh cao)',
                        data: [16, 90],
                        backgroundColor: '#007BFF',
                    }, {
                        label: 'Kodak (Sau đột phá số)',
                        data: [6, 7],
                        backgroundColor: '#DC3545',
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'So Sánh Hiệu Suất: Chuyển Đổi Thành Công vs. Thất Bại',
                            font: { size: 18, weight: 'bold' },
                            padding: { top: 10, bottom: 20 }
                        },
                        tooltip: {
                            callbacks: {
                                title: tooltipTitleCallback,
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    if (label) { label += ': '; }
                                    if (context.parsed.y !== null) {
                                        if (context.label.includes('%')) {
                                            label += context.parsed.y + '%';
                                        } else {
                                            label += '$' + context.parsed.y + 'B';
                                        }
                                    }
                                    return label;
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Giá trị'
                            }
                        }
                    }
                }
            });
        });
    </script>
</body>
</html>

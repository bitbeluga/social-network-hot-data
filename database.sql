CREATE TABLE `po_events`
(
    `id`          BIGINT(20) NOT NULL AUTO_INCREMENT,
    `title`       VARCHAR(100) NULL DEFAULT NULL COMMENT '事件标题' COLLATE 'utf8mb4_general_ci',
    `type`        TINYINT(4) NOT NULL COMMENT '数据来源类型 1-微博热搜 2-微博话题 3-今日头条 4-抖音 5-知乎 6-B站 7-百度',
    `last_rank` NULL DEFAULT 0 COMMENT '最新热度',
    `highest_rank` NULL DEFAULT 0 COMMENT '历史最高热度',
    `last_count`  BIGINT(20) NULL DEFAULT NULL COMMENT '最新热度',
    `rise_speed`  COMMENT '上升速度：指该热搜在榜时间内，其热度的平均增长速度。负数表热搜热度下降。',
    `create_time` DATETIME NOT NULL COMMENT '创建时间',
    `update_time` DATETIME NULL DEFAULT NULL COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE,
) COMMENT='舆论场事件信息表'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;

CREATE TABLE `po_event_time_data`
(
    `id`          BIGINT(20) NOT NULL AUTO_INCREMENT,
    `event_id`    BIGINT(20) NOT NULL COMMENT '事件 ID',
    `rank`        TINYINT(4) NOT NULL COMMENT '排名',
    `count`       INT(20) NOT NULL COMMENT '热度',
    `create_time` DATETIME NOT NULL COMMENT '创建时间',
    PRIMARY KEY (`id`) USING BTREE,
) COMMENT='舆论场事件的时序数据表'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;

CREATE TABLE `po_user`
(
    `id`              BIGINT(20) NOT NULL AUTO_INCREMENT,
    `open_id`         VARCHAR(100) NOT NULL COMMENT '微信用户open_id' COLLATE 'utf8mb4_general_ci',
    `nick_name`       VARCHAR(50) NULL DEFAULT NULL COMMENT '用户昵称' COLLATE 'utf8mb4_general_ci',
    `real_name`       VARCHAR(50) NULL DEFAULT NULL COMMENT '真实姓名' COLLATE 'utf8mb4_general_ci',
    `mobile`          VARCHAR(20) NULL DEFAULT NULL COMMENT '手机号' COLLATE 'utf8mb4_general_ci',
    `status`          TINYINT(4) NOT NULL DEFAULT '1' COMMENT '用户状态 1-正常 2-禁用',
    `last_login_time` DATETIME NULL DEFAULT NULL COMMENT '上次登录时间',
    `create_time`     DATETIME     NOT NULL COMMENT '创建时间',
    `create_user`     VARCHAR(50) NULL DEFAULT NULL COMMENT '创建用户' COLLATE 'utf8mb4_general_ci',
    `update_time`     DATETIME NULL DEFAULT NULL COMMENT '更新时间',
    `update_user`     VARCHAR(50) NULL DEFAULT NULL COMMENT '更新用户' COLLATE 'utf8mb4_general_ci',
    PRIMARY KEY (`id`) USING BTREE,
    UNIQUE INDEX `open_id` (`open_id`) USING BTREE
) COMMENT='舆论场用户表'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB

CREATE TABLE `po_user_collect`
(
    `id`          BIGINT(20) NOT NULL AUTO_INCREMENT,
    `user_id`     BIGINT(20) NOT NULL COMMENT '用户ID',
    `event_id`    BIGINT(20) NOT NULL COMMENT '事件ID',
    `has_delete`  TINYINT(4) NOT NULL DEFAULT '0' COMMENT '是否删除 0-否 1-是',
    `create_time` DATETIME NOT NULL COMMENT '创建时间',
    `update_time` DATETIME NULL DEFAULT NULL COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE,
    UNIQUE INDEX `user_event` (`user_id`, `event_id`) USING BTREE,
) COMMENT='舆论场用户收藏事件表'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB